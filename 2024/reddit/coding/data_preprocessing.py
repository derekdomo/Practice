'''General Guide: https://www.kaggle.com/code/durgancegaur/a-guide-to-any-classification-problem'''


# Look at data types
df.dtypes

# Convert Object to String
string_col = df.select_dtypes(include="object").columns
df[string_col]=df[string_col].astype("string")


# Get categorical features
string_col=df.select_dtypes("string").columns.to_list()
num_col=df.columns.to_list()
#print(num_col)
for col in string_col:
    num_col.remove(col)
num_col.remove("HeartDisease")

# Look at the numerical feature stats
df.describe().T


# Summarize the features and see if there are any abnormal places like outliers



# EDA
## Correlation matrix
import plotly.express as px
px.imshow(df.corr(),title="Correlation Plot of the Heat Failure Prediction")


# Check distribution
from matplotlib import pyplot as plt
plt.figure(figsize=(15,10))
for i,col in enumerate(df.columns,1):
    plt.subplot(4,3,i)
    plt.title(f"Distribution of {col} Data")
    sns.histplot(df[col],kde=True)
    plt.tight_layout()
    plt.plot()


# Preprocessing
## Checking for Type of data
df.info()

## Check nulls
df.isnull().sum()

## Impute
from sklearn.impute import SimpleImputer

## normalization
scaler = preprocessing.RobustScaler()
robust_df = scaler.fit_transform(x)
robust_df = pd.DataFrame(robust_df, columns =['x1', 'x2'])

scaler = preprocessing.StandardScaler()
standard_df = scaler.fit_transform(x)
standard_df = pd.DataFrame(standard_df, columns =['x1', 'x2'])

scaler = preprocessing.MinMaxScaler()
minmax_df = scaler.fit_transform(x)
minmax_df = pd.DataFrame(minmax_df, columns =['x1', 'x2'])

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer = imputer.fit(df[['Weight']])
df['Weight'] = imputer.transform(df[['Weight']])


'''train test split with stratify'''
from sklearn.model_selection import train_test_split

train, validate = train_test_split(
        raw_data, test_size=0.1, random_state=seed, stratify=raw_data['label']



'''
One hot encoder
'''
## Creaeting one hot encoded features for working with non tree based algorithms 
df_nontree=pd.get_dummies(df, columns=string_col, drop_first=False)
df_nontree.head()


'''
Cross Validation
'''
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,classification_report,accuracy_score,roc_auc_score
from sklearn.preprocessing import RobustScaler,MinMaxScaler,StandardScaler
acc_log=[]

kf=model_selection.StratifiedKFold(n_splits=5)
for fold , (trn_,val_) in enumerate(kf.split(X=df_nontree,y=y)):

    X_train=df_nontree.loc[trn_,feature_col_nontree]
    y_train=df_nontree.loc[trn_,target]

    X_valid=df_nontree.loc[val_,feature_col_nontree]
    y_valid=df_nontree.loc[val_,target]

    #print(pd.DataFrame(X_valid).head())
    ro_scaler=MinMaxScaler()
    X_train=ro_scaler.fit_transform(X_train)
    X_valid=ro_scaler.transform(X_valid)


    clf=LogisticRegression()
    clf.fit(X_train,y_train)
    y_pred=clf.predict(X_valid)
    print(f"The fold is : {fold} : ")
    print(classification_report(y_valid,y_pred))
    acc=roc_auc_score(y_valid,y_pred)
    acc_log.append(acc)
    print(f"The accuracy for Fold {fold+1} : {acc}")
    pass






