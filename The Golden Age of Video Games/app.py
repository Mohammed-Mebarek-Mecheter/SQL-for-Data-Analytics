import streamlit as st
import pandas as pd
import plotly.express as px
import os

# Define file paths for data
data_folder = 'datasets'
game_sales_path = os.path.join(data_folder, 'game_sales.csv')
game_reviews_path = os.path.join(data_folder, 'game_reviews.csv')
top_critic_scores_path = os.path.join(data_folder, 'top_critic_scores.csv')
top_critic_scores_more_than_four_games_path = os.path.join(data_folder, 'top_critic_scores_more_than_four_games.csv')
top_user_scores_more_than_four_games_path = os.path.join(data_folder, 'top_user_scores_more_than_four_games.csv')


# Load data using caching
@st.cache_data
def load_data():
    game_sales = pd.read_csv(game_sales_path)
    game_reviews = pd.read_csv(game_reviews_path)
    top_critic_scores = pd.read_csv(top_critic_scores_path)
    top_critic_scores_more_than_four_games = pd.read_csv(top_critic_scores_more_than_four_games_path)
    top_user_scores_more_than_four_games = pd.read_csv(top_user_scores_more_than_four_games_path)
    return game_sales, game_reviews, top_critic_scores, top_critic_scores_more_than_four_games, top_user_scores_more_than_four_games


# Define functions for each page
def show_top_selling_games(data):
    st.header('Top Selling Games')
    fig = px.bar(data.head(10), x='Name', y='Total_Shipped')
    st.write(fig)


def show_critic_scores(data):
    st.header('Critic Scores')
    st.dataframe(data.head(10))


def show_user_scores(data):
    st.header('User Scores')
    st.dataframe(data.head(10))


def show_sales_analysis(data):
    st.header('Sales Analysis')

    # Analyze and prepare data for visualizations
    # Example: Group data by year and calculate average sales
    year_wise_avg_sales = data.groupby('Year')['Total_Shipped'].mean()

    # Create visualizations
    # Example 1: Line chart for average sales over years
    fig_avg_sales_over_years = px.line(year_wise_avg_sales, x=year_wise_avg_sales.index, y=year_wise_avg_sales.values)
    st.write("Average Sales per Year")
    st.write(fig_avg_sales_over_years)

    # Top publishers by total shipped games
    top_publishers = data.groupby('Publisher')['Total_Shipped'].sum().sort_values(ascending=False)[:10]

    # Bar chart for top publishers
    fig_top_publishers = px.bar(top_publishers, x=top_publishers.index, y=top_publishers.values)
    st.write("Top Publishers by Total Shipped")
    st.write(fig_top_publishers)

    top_developers = data.groupby('Developer')['Total_Shipped'].sum().sort_values(ascending=False)[:10]

    fig_top_developers = px.bar(top_developers, x=top_developers.index, y=top_developers.values)
    st.write("Top Developers by Total Shipped")
    st.write(fig_top_developers)


# Main app logic
def main():
    st.title('Video Game Analysis Dashboard')

    # Sidebar navigation
    selected_page = st.sidebar.selectbox('Choose a page:', ['Top Selling Games', 'Critic Scores', 'User Scores', 'Sales Analysis'])

    # Load data
    game_sales, game_reviews, top_critic_scores, top_critic_scores_more_than_four_games, top_user_scores_more_than_four_games = load_data()

    # Display selected page content
    if selected_page == 'Top Selling Games':
        show_top_selling_games(game_sales.copy())  # Avoid modifying original data
    elif selected_page == 'Critic Scores':
        show_critic_scores(top_critic_scores.copy())
    elif selected_page == 'User Scores':
        show_user_scores(top_user_scores_more_than_four_games.copy())
    elif selected_page == 'Sales Analysis':
        show_sales_analysis(game_sales.copy())

    # Error handling (optional, but good practice)
    try:
        # Your app logic here
        pass
    except Exception as e:
        st.error(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
