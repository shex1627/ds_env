# makes python code to notebook snippets
"""
to-do:
    load snippets as individual json files instead putting all snippets in a single script
"""

snippets_file_path = '<jupyter config path>Jupyter/nbextensions/snippets/snippets.json'

pandas_snippets = {
    'name':'pd_np_plt',
    'code': [
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt"
    ]
}

markdown_font_snippets = {
    'name': 'markdown_font',
    'code': [
        "from IPython.core.display import display, HTML",
        "display(HTML('<style>.rendered_html { font-size: 15px; }</style>'))"
    ]
}

js_divergence = {
    'name': "js_divergence",
    'code': [
        "def jsd(x,y): #Jensen-shannon divergence",
            "import warnings",
            "warnings.filterwarnings('ignore', category = RuntimeWarning)",
            "x = np.array(x)",
            "y = np.array(y)",
            "d1 = x*np.log2(2*x/(x+y))",
            "d2 = y*np.log2(2*y/(x+y))",
            "d1[np.isnan(d1)] = 0",
            "d2[np.isnan(d2)] = 0",
            "d = 0.5*np.sum(d1+d2)",
            "return np.round(d, 5)"
    ]
}

counter = {
    'name': 'counter',
    'code': ['from collections import Counter']
}

max_col_width = {
    'name': 'max_col_width',
    'code':["pd.set_option('display.max_colwidth', -1)"]
}

json_dump = {
    'name' : 'json_dump',
    'code' : [
        "with open('', 'w') as file:",
        "    json.dump(, file)"
    ]
}

make_excel = {
    'name' : 'make_excel',
    'code' : [
        "with pd.ExcelWriter('output.xlsx') as writer:",
        "    df1.to_excel(writer, sheet_name='Sheet_name_1')",
        "    df2.to_excel(writer, sheet_name='Sheet_name_2')"
    ]
}

tsne = {
    'name': 'tsne',
    'code': """from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, verbose=0, perplexity=40, n_iter=250)
tsne_results = tsne.fit_transform(matrix) #'matrix' """.split("\n")
}

tsne_plotly_plot = {
    'name' : 'tsne_plotly_plot',
    'code' : """import plotly.express as px

#### data processing
group_col = '' # column to be grouped_by
temp_df = dfs[i][list(cols) + [group_col]]
temp_df['tsne1'] = tsne_results[:,0]
temp_df['tsne2'] = tsne_results[:,1]
temp_df['text'] = temp_df[list(cols)].apply(lambda row: "||".join(str(num) for num in list(row)), axis=1)


#### using plotly
fig = px.scatter(temp_df, x="tsne1", y="tsne2", color=group_col,
                  hover_data=["text"])

fig.show()""".split("\n")
}

snippets = {
    'snippets': [pandas_snippets, max_col_width, json_dump, counter, 
                 tsne, tsne_plotly_plot,
                 js_divergence,  markdown_font_snippets, make_excel]
}

import json
snippets_json = json.dumps(snippets)
snippets_json

with open(snippets_file_path, 'w') as outfile:  
    json.dump(snippets, outfile)
