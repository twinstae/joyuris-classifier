import streamlit as st
import pandas as pd
from math import pi

from PIL import Image
from bokeh.plotting import figure
from bokeh.transform import cumsum
from model import predict


def create_pie_chart(probability_dict):
    data = pd.Series(probability_dict).reset_index(name='value').rename(columns={'index': 'candidate'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = ['#ccebc5', '#fed9a6', '#ffffcc']

    print(data)

    p = figure(plot_height=350, title="신경망이 예측한 확률 비율", toolbar_location=None,
               tools="hover", tooltips="@candidate: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='candidate', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None
    st.bokeh_chart(p, use_container_width=False)


st.title("조유리즈 판별기")
uploaded_file = st.file_uploader("얼굴만 자른 사진을 올려주세요...", type="jpg")
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    prediction, probability = predict(img)
    st.image(
        img,
        width=256,
        caption=f"이 사람은... {prediction}!",
    )

    create_pie_chart(probability)
