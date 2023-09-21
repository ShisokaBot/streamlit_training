import streamlit as st
import pandas as pd
from PIL import Image

# title
st.title('This is the TITLE')
st.caption('This is the caption')

# header
st.header('This is the header')
st.subheader('This is the subheader')
st.text('text')
st.write('write')

# magic command
"""
# h1
## h2
### h3
#### h4

    python
import streamilit as st

# title
st.title('This is the TITLE')
st.caption('This is the caption')
"""

# code
code_python = """
#Python
print("Python")
"""

code_java = """
// Java
System.out.println("Java");
"""
st.code(code_java, language='java')

code_php = """
// PHP
echo 'PHP';
"""
st.code(code_php, language='PHP')

code_ruby = """
# Ruby
puts 'Ruby'
"""
st.code(code_ruby, language='ruby')

code_sh = """
$ streamlit hello
"""
st.code(code_sh, language='sh')

# markdown
st.markdown('This is **_italic_**.')
st.markdown(':green(緑色)です')
st.markdown('これは **:red[赤色で太字]** です')

'This is **_italic_**.'
':green(緑色)です'
'これは **:red[赤色で太字]** です'

# DataFrame
df = pd.DataFrame([3,2,4,2],
                  ['りんご', 'みかん', 'いちご', 'もも'],
                  ['売上'],)
print(df)

