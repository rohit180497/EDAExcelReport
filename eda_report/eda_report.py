import pandas as pd
import numpy as np
import os
from EDA_report.eda_report.eda_format import EDA_Formatter 
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

from sklearn.model_selection import StratifiedKFold
from sklearn import metrics

class EDAReport():

    def __init__(self, data, target, report_path, ignore_cols= None, cat_label_enco_thresh= 0.05, num_min_samples_leaf = 0.1, conditional_color: str = 'red' ):
        grp_data = self._get_full_eda(
            data, target, ignore_cols, cat_label_enco_thresh, num_min_samples_leaf)
        
        roc_data = self._get_roc_auc(
            data, target, ignore_cols, cat_label_enco_thresh, num_min_samples_leaf
        )
        
        xw = pd.ExcelWriter(report_path, engine='openpyxl')
        roc_data.to_excel(xw, sheet_name = 'ROC Report', index= False)
        grp_data.to_excel(xw, sheet_name = 'Detailed EDA', index =  False)
        xw.close()
        EDA_Formatter(path =  report_path, model_type= target, 
                      conditional_color = conditional_color)

    
    def _get_full_eda(self, data, target, ignore_cols= None, cat_label_enco_thresh= 0.05, num_min_samples_leaf =0.01):
        cols = data.columns.tolist()
        cols.remove(target)



        if ignore_cols is not None:
            cols= [col for col in cols if col not in ignore_cols]
        
        y = data[target].copy()

        # Check for binary columns and replace 0 with "No" and 1 with "Yes"
        for col in cols:
            unique_values = set(data[col].dropna().unique())
            if unique_values == {0, 1}:
                data[col] = data[col].map({0: "No", 1: "Yes"}).fillna("No" if 0 in unique_values else "Yes")
            elif unique_values == {'Y', 'N'}:
                data[col] = data[col].map({'Y': "Yes", 'N': "No"}).fillna("No" if 'N' in unique_values else "Yes")

        # EDA

        all_grp_dfs = []

        for col in cols:

            #numeric
            isnum = str(data[col].dtype).startswith('float') | str(data[col].dtype).startswith('int')

            if isnum:
                X = np.array(data[col].fillna(data[col].median()
                                              ).values.tolist()).reshape(-1,1)
                dt =  DecisionTreeClassifier(class_weight='balanced', min_samples_leaf= num_min_samples_leaf)
                dt.fit(X, y)

                thresholds = np.sort(np.unique(dt.tree_.threshold))
                thresholds = np.append(thresholds, np.inf)
                X = np.digitize(X, thresholds, right= True)

                x_map = dict(enumerate(map(str, thresholds)))

                grp_df = pd.DataFrame(X, columns= [col])
                grp_df[col] = grp_df[col].replace(x_map)
                grp_df['target'] = y

                grp_df = grp_df.groupby(col)[target].agg(
                ['count', 'sum', 'mean']).reset_index()
                grp_df.insert(0, 'Column', col)
                grp_df = grp_df.rename(columns = {col: "value"})
        
            else:
                grp_df  = data.groupby(col)[target].agg(
                    ['count', 'sum', 'mean']).reset_index()
                grp_df.insert(0, 'Column', col)
                grp_df = grp_df.rename(columns = {col: "value"})

            all_grp_dfs.append(grp_df)

        return pd.concat(all_grp_dfs)
    

    def _get_roc_auc(self, data, target, ignore_cols= None, cat_label_enco_thresh= 0.05, num_min_smaples_leaf = 0.1):

        # get all required columns
        cols = data.columns.tolist()
        cols.remove(target)

        if ignore_cols is not None:
            cols = [col for col in cols if col not in ignore_cols]

        y = data[target].copy()

        #EDA
        all_auc_dfs = []

        for col in cols:

            #numeric
            isnum = str(data[col].dtype).startswith('float') | str(data[col].dtype).startswith('int')

            if isnum:
                X = np.array(data[col].fillna(data[col].median()
                                              ).values.tolist()).reshape(-1,1)
                dt =  DecisionTreeClassifier(class_weight='balanced', min_samples_leaf= num_min_smaples_leaf)
            else:
                X = np.array(data[col].fillna(data[col].mode()[0]
                                              ).values.tolist()).reshape(-1,1)
                
                label_enc = {}
                i = 0

                for unx in np.unique(X):
                    rate = np.where(X== unx, 1, 0).sum()/ len(X)
                    
                    if rate >= cat_label_enco_thresh:
                        i = i+1
                        label_enc.update({unx: i})
                    else:
                        label_enc.update({unx: 0})

                map_label_enc = np.vectorize(label_enc.get)

                X = map_label_enc(X)
                dt = DecisionTreeClassifier(class_weight='balanced')

            #K-fold decision tree classifier

            kf =  StratifiedKFold(n_splits= 10, random_state= None, shuffle= False)
            results = []
            i = 0

            for train_index, test_index in kf.split(X, y):
                X_train, X_test = X[train_index], X[test_index]
                y_train, y_test = y.iloc[train_index], y.iloc[test_index]
                i = i +1
                dt.fit(X_train, y_train)
                yproba = dt.predict_proba(X_test)
                auc = metrics.roc_auc_score(y_test, yproba[:, 1])
                results.append(auc)

            all_auc_dfs.append({
                "Column": col,
                "ROC AUC": np.median(results)
            })


        return pd.DataFrame(all_auc_dfs)   







