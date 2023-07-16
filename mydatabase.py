import streamlit as st
import pandas as pd

class MyDashboard():
    def __init__(self, df=None):
        super(MyDashboard, self).__init__()
        self.df = df

        if self.df == None:
            self.ReadDataBase()            
        
        btn = st.sidebar.button("Click")
        cmb = st.sidebar.ComboBox()
        if btn:
            self.TesteClick()
        
    def ReadDataBase(self):
        self.df = pd.read_csv(r"db/vgsales.csv")
        print("Teste")
        
   
    def TesteClick(self):
        print("Click button")
        st.bar_chart(self.df[["Platform","Rank", "Year"]], x="Platform",y="Year")

if __name__ == "__main__":
    MyDashboard()