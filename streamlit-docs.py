# BASIC CONCEPTS

"""
# My first app
Here's our first attempt at using data to create a table:
"""
import streamlit as st
import pandas as pd
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
df

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

import streamlit as st
import numpy as np

dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),                        # Tạo 10 hàng x 20 cột số ngẫu nhiên
    columns=('col %d' % i for i in range(20)))      # # → thay %d bằng i, ví dụ: 'col 0', 'col 1', ...

st.dataframe(dataframe.style.highlight_max(axis=0)) # Hiển thị bảng, tô đậm giá trị lớn nhất theo từng cột

import streamlit as st
import numpy as np
import pandas as pd

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.table(dataframe)

import streamlit as st 
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns = ['a', 'b', 'c'])
st.line_chart(chart_data)

import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    # 1000 điểm ngẫu nhiên, chia 50 để thu nhỏ độ phân tán, cộng tọa độ San Francisco để căn giữa bản đồ
    columns=['lat', 'lon'])   # Cột lat = vĩ độ, lon = kinh độ

st.map(map_data)              # Hiển thị 1000 điểm lên bản đồ

import streamlit as st
x = st.slider('x') # 👈 this is a widget
st.write(x, 'squared is', x * x)

import streamlit as st
st.text_input("Your name", key="name")
# You can access the value at any point with:
st.session_state.name

import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

"You selected: ", option

import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")
    
import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty() # latest_iteration — ô để hiện chữ (lúc đầu trống)
bar = st.progress(0) # bar - thanh tiến trình, bắt đầu ở 0%

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}') # mỗi vòng lặp, cập nhật ô chữ thành 'Iteration 1', 'Iteration 2', ... (dùng i + 1 vì i bắt đầu từ 0)
  bar.progress(i + 1) # Cập nhật thanh tiến trình lên 1%, 2%, 3%... tới 100%
  time.sleep(0.1) # Dừng 0.1 giây trước khi chạy vòng tiếp theo - để mắt người dùng thấy được sự thay đổi

'🎉...and now we\'re done!' # Sau khi vòng lặp xong, hiện chữ "...and now we're done!"

# ADVANCED CONCEPTS

@st.cache_data
def long_running_function(param1, param2):
    return ...

import streamlit as st 
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    
st.session_state.counter += 1

st.header(f'This page has run {st.session_state.counter} times.')
st.button('Run it again')

import streamlit as st
import numpy as np
import pandas as pd
if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame(np.random.randn(20, 2), columns=['X', 'Y'])
st.header('Choose a datapoint color')
color = st.color_picker('Color', '#FF0000')
st.divider()
st.scatter_chart(st.session_state.df, x='X', y='Y', color=color)


# import streamlit as st
# conn = st.connection("my_database")
# df = conn.query("select * from my_table")
# st.dataframe(df)

import streamlit as st
 # Define the pages
main_page = st.Page('main_page.py', title='Main Page', icon='🎈')
page_2 = st.Page('page_2.py', title='Page 2', icon='❄️')
page_3 = st.Page('page_3.py', title='Page 3', icon='🎉')
 # Set up navigation
pg = st.navigation([main_page, page_2, page_3])
 # Run the selected page
pg.run()