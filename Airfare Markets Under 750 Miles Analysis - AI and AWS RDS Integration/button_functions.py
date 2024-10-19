from PyQt6.QtWidgets import QMessageBox
import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
from openai import OpenAI

# Load the .env file
load_dotenv()


class Buttons:
    
    @staticmethod
    def connect_database():
        
        #call env
        db_host = os.getenv('DB_HOST')
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_name = os.getenv('DB_NAME')
        db_port = os.getenv('DB_PORT')
        
        try:
            # Establishing the connection to RDS PostgreSQL
            connection = psycopg2.connect(
            host=db_host,
            database=db_name,
            user=db_user,
            password=db_password,
            port=db_port
            )
    
            cursor = connection.cursor()
            print("Connected to AWS RDS PostgreSQL")
            return cursor

        except Exception as error:
            QMessageBox.critical(None, "Error", str(error), QMessageBox.StandardButton.Ok)
    
    
    @staticmethod
    def connect_ai(df_str, instruction):
        openai = os.getenv('CHATGPT_API')
        client = OpenAI(api_key=openai)

        completion = client.chat.completions.create(
            model="gpt-4",
           messages=
           [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content":  f"Here is a dataset:\n\n{df_str}\n\n"
                                f"Here is what action I want you to perform in the database:\n\n{instruction}\n\n"
                        "Conduct a detailed data analysis by examining the dataset provided, "
                        "identifying patterns, trends, and any anomalies. Offer insights based on "
                        "statistical evidence to support conclusions drawn from the data.\n\n"
                        "# Steps\n\n"
                        "Special Instruction, Do not give me this during my question: 1. **Understand the Dataset**: Carefully review the dataset to understand its structure, types of variables, and any metadata provided.\n"
                        "Special Instruction, Do not give me this during my question: 2. **Data Cleaning**: Identify and clean any missing, duplicate, or inconsistent data points.\n"
                        "Special Instruction, Do not give me this during my question: 3. **Descriptive Analysis**: Summarize the main features of the dataset using statistics such as mean, median, mode, standard deviation, etc.\n"
                        "Special Instruction, Do not give me this during my question: 4. **Exploratory Data Analysis**: Use graphical representations like histograms, scatter plots, and boxplots to visualize trends, distributions, and relationships within the data.\n"
                        "Special Instruction, Do not give me this during my question: 5. **Statistical Testing**: Perform appropriate statistical tests to validate hypotheses. State the null and alternative hypotheses before conducting tests.\n"
                        "Special Instruction, Do not give me this during my question: 6. **Anomaly Detection**: Investigate and highlight any anomalies or outliers and discuss their potential impact.\n"
                        "Special Instruction, Do not give me this during my question: 7. **Conclusions and Insights**: Draw conclusions from the analysis, supported by evidence from the dataset. Offer insightful recommendations or predictions based on the findings.\n\n"
                        "If i ask a question that doesnt pertain to the database, it's ok you can answer normally, for example, if i ask how are you, or what are you, you can freely respond"
                        "If i ask to give me all the rows, give me all the rows in a python dataframe form"
                        "# Output Format\n\n"
                        "Only provide me the answer that I'm looking for, keep the answer short without giving full sentences\n"
                        "For example, if i ask what year is stored in the system, this is when you will look at the dataframe I attached and look for that year column\n"
                        "another instruction: mkt_fare column is market fare\n"
                        "another instruction: city1 is the city the flight is coming from and city2 is the city going to\n"
                        "KEEP YOU ANSWER SHORT, SUPER SHORT"
                        

                }
            ],
        )

        return completion.choices[0].message.content
    
                
    def Search_Button_Clicked(self):

        #retrieve the text from the textbox
        user_input = self.UserInput_TextEdit.toPlainText()
        
        #connect to the database
        cursor = Buttons.connect_database()
        select_query = "SELECT year, mkt_fare, city1, city2 FROM airline_analysis WHERE year = 2024 LIMIT 10"
        cursor.execute(select_query)
        results = cursor.fetchall()
        
        # Fetch column names from the cursor description
        columns = [desc[0] for desc in cursor.description]
        
        #convert to the dataframe
        dataframe = pd.DataFrame(results, columns=columns)
        print(dataframe)
        
        #Insert the result to execute the AI request
        result = Buttons.connect_ai(dataframe, user_input)

        
        self.AI_Result_TextEdit.setText(result)
        
        self.UserInput_TextEdit.clear()

    def Clear_Button_Clicked(self):
        self.UserInput_TextEdit.clear()
    
    