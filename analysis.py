# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 09:48:38 2020

@author: Florian Jehn
"""
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import MaxNLocator
import seaborn as sns

# Create the barplots for all categorical topics
kinds = {"group_activities":"Activities", "group_contacts":"Contacts", "group_topics":"Topics", "support_needs":"Support Needs"}
for key, val in kinds.items():
    activities = pd.read_csv(key + ".csv", sep=";", encoding="'latin-1'")

    ax = activities.sum().sort_values().plot(kind="barh", color="#0A6B7C", zorder=5)
    # Add labels
    ax.set_title(val, alpha=0.7)
    ax.set_xlabel("Times Mentioned", alpha=0.7)
    # Everything after this is just for layout. 
    ax.xaxis.grid(True, color="lightgrey")
    ax.tick_params(axis=u'both', which=u'both',length=0)
    for spine in ax.spines.values():
            spine.set_visible(False)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.setp(ax.get_xticklabels(), alpha=0.7)
    plt.setp(ax.get_yticklabels(), alpha=0.7)
    fig = plt.gcf()
    fig.tight_layout()
    fig.set_size_inches(5,3)
    plt.savefig(key+".png", dpi=200, bbox_inches="tight")
    plt.close()

# Create the plots for the numerical topics
meta = pd.read_csv("group_meta.csv", sep=";", encoding="'latin-1'")
main = meta[['Number of core group members', 'Number of total group members',
       'Founding year', 
       'Meetings per month', 
       'CEA Funding']]
main.columns = map(str.title, main.columns)



fig, axes = plt.subplots(nrows=5)
for ax, col in zip(axes, main.columns):
    ax = sns.swarmplot(x=col,data=main,color="#0A6B7C", zorder=6,ax=ax)
    plt.setp(ax.get_xticklabels(), alpha=0.7)
    plt.setp(ax.get_yticklabels(), alpha=0.7)
    ax.set_title(col, alpha=0.7)    
    ax.set_xlabel("")

#    ax.xaxis.grid(True, color="lightgrey", zorder=0)
    ax.tick_params(axis=u'both', which=u'both',length=0)
    for spine in ax.spines.values():
            spine.set_color("grey")
            
            
fig.set_size_inches(12,6)
fig.tight_layout()
plt.savefig("meta_1.png", dpi=200)
plt.close()


# sum_plots = meta[['Future existence of group in doubt','University group', 'registered society']]
# ax = sum_plots.sum().sort_values().plot(kind="barh")
# ax.set_title("Meta 2")
# fig = plt.gcf()
# fig.tight_layout()
# plt.savefig("meta_2.png", dpi=200)
# plt.close()
