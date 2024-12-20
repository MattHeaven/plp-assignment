import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Optional, Tuple
import numpy as np

class DataAnalyzer:
    """A class to handle data loading, analysis, and visualization"""
    
    def __init__(self, file_path: str):
        """Initialize the analyzer with a file path"""
        self.file_path = file_path
        self.data: Optional[pd.DataFrame] = None
        
    def load_data(self) -> None:
        """Load and clean the dataset"""
        try:
    
            self.data = pd.read_csv(self.file_path)
            print("Data loaded successfully!")
           
            print("\nDataset Overview:")
            print(f"Shape: {self.data.shape}")
            print("\nFirst few rows:")
            print(self.data.head())
            
         
            missing_values = self.data.isnull().sum()
            if missing_values.any():
                print("\nMissing values found:")
                print(missing_values[missing_values > 0])
                
                # Fill missing numerical values with median
                numeric_columns = self.data.select_dtypes(include=[np.number]).columns
                for col in numeric_columns:
                    self.data[col].fillna(self.data[col].median(), inplace=True)
                    
                # Fill missing categorical values with mode
                categorical_columns = self.data.select_dtypes(include=['object']).columns
                for col in categorical_columns:
                    self.data[col].fillna(self.data[col].mode()[0], inplace=True)
                    
                print("\nMissing values handled.")
            
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            raise
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise
            
    def perform_analysis(self) -> None:
        """Perform basic statistical analysis"""
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            print("\nBasic Statistics:")
            print(self.data.describe())
            
            # Group by analysis (assuming 'Platform' and 'Global_Sales' columns exist)
            platform_analysis = self.data.groupby('Platform')['Global_Sales'].agg([
                'count', 'mean', 'sum'
            ]).sort_values('sum', ascending=False)
            
            print("\nSales by Platform:")
            print(platform_analysis)
            
        except Exception as e:
            print(f"Error during analysis: {str(e)}")
            
    def create_visualizations(self) -> None:
        """Create various visualizations of the data"""
        if self.data is None:
            print("No data loaded. Please load data first.")
            return
            
        try:
            
            plt.style.use('seaborn')
            
      
            fig = plt.figure(figsize=(20, 15))
            
          
            plt.subplot(2, 2, 1)
            yearly_sales = self.data.groupby('Year')['Global_Sales'].sum()
            yearly_sales.plot(kind='line', marker='o')
            plt.title('Global Video Game Sales Trend Over Years')
            plt.xlabel('Year')
            plt.ylabel('Global Sales (millions)')
            
        
            plt.subplot(2, 2, 2)
            platform_sales = self.data.groupby('Platform')['Global_Sales'].sum()
            platform_sales.nlargest(10).plot(kind='bar')
            plt.title('Top 10 Gaming Platforms by Global Sales')
            plt.xlabel('Platform')
            plt.ylabel('Total Global Sales (millions)')
            plt.xticks(rotation=45)
            
          
            plt.subplot(2, 2, 3)
            plt.hist(self.data['Global_Sales'], bins=50, edgecolor='black')
            plt.title('Distribution of Global Sales')
            plt.xlabel('Global Sales (millions)')
            plt.ylabel('Frequency')
            
            # 
            plt.subplot(2, 2, 4)
            plt.scatter(self.data['NA_Sales'], self.data['EU_Sales'], alpha=0.5)
            plt.title('North America vs Europe Sales Comparison')
            plt.xlabel('North America Sales (millions)')
            plt.ylabel('Europe Sales (millions)')
            
            
            plt.tight_layout()
            plt.show()
            
           
            plt.figure(figsize=(12, 6))
            genre_counts = self.data['Genre'].value_counts()
            sns.barplot(x=genre_counts.values, y=genre_counts.index)
            plt.title('Distribution of Games by Genre')
            plt.xlabel('Number of Games')
            plt.show()
            
        except Exception as e:
            print(f"Error creating visualizations: {str(e)}")
            
def main():
    
    file_path = 'vgsales.csv' 
    
    
    analyzer = DataAnalyzer(file_path)
    
    try:
        
        analyzer.load_data()
        
       
        analyzer.perform_analysis()
        
       
        analyzer.create_visualizations()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        
if __name__ == "__main__":
    main()
