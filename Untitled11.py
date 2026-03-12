#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

df = pd.read_csv("KDDTest+.txt", header=None)

df.shape
df.head()


# In[6]:


df[41].value_counts()


# In[7]:


df = df.drop_duplicates()


# In[8]:


import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x=df[41])
plt.xticks(rotation=90)
plt.show()


# In[9]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split


# In[11]:


df = pd.read_csv("KDDTest+.txt", header=None)

print(df.shape)
df.head()


# In[13]:


columns = [
'duration','protocol_type','service','flag','src_bytes','dst_bytes','land',
'wrong_fragment','urgent','hot','num_failed_logins','logged_in',
'num_compromised','root_shell','su_attempted','num_root','num_file_creations',
'num_shells','num_access_files','num_outbound_cmds','is_host_login',
'is_guest_login','count','srv_count','serror_rate','srv_serror_rate',
'rerror_rate','srv_rerror_rate','same_srv_rate','diff_srv_rate',
'srv_diff_host_rate','dst_host_count','dst_host_srv_count',
'dst_host_same_srv_rate','dst_host_diff_srv_rate',
'dst_host_same_src_port_rate','dst_host_srv_diff_host_rate',
'dst_host_serror_rate','dst_host_srv_serror_rate',
'dst_host_rerror_rate','dst_host_srv_rerror_rate','label','difficulty'
]

df.columns = columns


# In[14]:


df = df.drop('difficulty', axis=1)


# In[15]:


sns.countplot(x=df['label'])
plt.xticks(rotation=90)
plt.title("Class Distribution")
plt.show()


# In[16]:


sns.countplot(x=df['label'])
plt.xticks(rotation=90)
plt.title("Class Distribution")
plt.show()


# In[17]:


class_counts = df['label'].value_counts()

print(class_counts)


# In[18]:


imbalance_ratio = class_counts.max() / class_counts.min()

print("Imbalance Ratio:", imbalance_ratio)


# In[19]:


total_samples = len(df)

minority_report = (class_counts / total_samples) * 100

print(minority_report)


# In[20]:


categorical_cols = ['protocol_type','service','flag']

encoder = LabelEncoder()

for col in categorical_cols:
    df[col] = encoder.fit_transform(df[col])


# In[21]:


df['label'] = LabelEncoder().fit_transform(df['label'])


# In[22]:


scaler = MinMaxScaler()

features = df.drop('label', axis=1)

scaled_features = scaler.fit_transform(features)

X = pd.DataFrame(scaled_features, columns=features.columns)
y = df['label']


# In[23]:


X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42
)

print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)


# In[24]:


plt.figure(figsize=(15,10))

sns.heatmap(
    df.corr(),
    cmap='coolwarm'
)

plt.title("Feature Correlation Heatmap")
plt.show()


# In[25]:


clean_df = pd.concat([X, y], axis=1)

clean_df.to_csv("NSL_KDD_CLEANED.csv", index=False)


# In[ ]:




