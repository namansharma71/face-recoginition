from graphviz import Digraph

# Create a new directed graph
dot = Digraph()

# Define nodes for the flowchart
dot.node('Start', 'Start')
dot.node('Data Collection', 'Data Collection\n(Sensors, APIs)')
dot.node('Data Processing', 'Data Processing\n(Data Analytics, Machine Learning)')
dot.node('Crop Recommendations', 'Crop Recommendations\n(Tailored Suggestions)')
dot.node('Resource Management', 'Resource Management\n(Optimized Water, Soil)')
dot.node('Market Insights', 'Market Insights\n(Real-Time Data)')
dot.node('User Interface', 'User Interface\n(Mobile/Web App)')
dot.node('User Feedback', 'User Feedback\n(Reviews, Ratings)')
dot.node('End', 'End')

# Define edges between nodes
dot.edge('Start', 'Data Collection')
dot.edge('Data Collection', 'Data Processing')
dot.edge('Data Processing', 'Crop Recommendations')
dot.edge('Data Processing', 'Resource Management')
dot.edge('Data Processing', 'Market Insights')
dot.edge('Crop Recommendations', 'User Interface')
dot.edge('Resource Management', 'User Interface')
dot.edge('Market Insights', 'User Interface')
dot.edge('User Interface', 'User Feedback')
dot.edge('User Feedback', 'End')

# Save and render the flowchart to a file
dot.render('harvesthero_workflow', format='png', cleanup=True)

print("Flowchart generated and saved as 'harvesthero_workflow.png'.")