# Databricks notebook source
# MAGIC %md
# MAGIC # Step-by-Step Deployment Guide for ThoughtSpot Companion Artifacts

# COMMAND ----------

# MAGIC %md 
# MAGIC 1. Set up Partner Connect for ThoughtSpot
# MAGIC 2. Set up connection for your result database 
# MAGIC 	The database name is user-specific in this case. Please look for the <your_name>_dns database in the Hive Metastore of your Databricks workspace.
# MAGIC 3. Once in ThoughtSpot, look for the connection just created on the Data - Connections tab. Rename it to Databricks-DNS
# MAGIC 4. Update the Databricks-DNS connection and add all the columns in the following 3 tables. 
# MAGIC 5. Import the .tml files in the /ThoughtSpot folder of this repo. 
# MAGIC 6. Viola! You now have a Liveboard to visualize and interact with the data in your Security delta lake.
# MAGIC 
# MAGIC 
# MAGIC Screenshots to be added

# COMMAND ----------


