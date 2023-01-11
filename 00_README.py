# Databricks notebook source
# MAGIC %md 
# MAGIC You may find this series of notebooks at https://github.com/databricks-industry-solutions/dns-analytics. For more information about this solution accelerator, visit https://www.databricks.com/solutions/accelerators/threat-detection.

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # Detecting Criminals and Nation States through DNS Analytics
# MAGIC 
# MAGIC You are a security practitioner, a data scientist or a security data engineer; you’ve seen the Large Scale Threat Detection and Response talk with Databricks . But you're wondering, “how can I try Databricks in my own security operations?” In this blog post, you will learn how to detect a remote access trojan using passive DNS (pDNS) and threat intel. Along the way, you’ll learn how to store, and analyze DNS data using Delta, Spark and MLFlow. As you well know, APT’s and cyber criminals are known to utilize DNS. Threat actors use the DNS protocol for command and control or beaconing or resolution of attacker domains. This is why academic researchers and industry groups advise security teams to collect and analyze DNS events to hunt, detect, investigate and respond to threats.  But you know, it's not as easy as it sounds.
# MAGIC 
# MAGIC The Complexity, cost, and limitations of legacy technology make detecting DNS security threats challenging for most enterprise organizations.
# MAGIC 
# MAGIC <img src='https://www.databricks.com/wp-content/uploads/2020/10/blog-detecting-criminals-1.png'>
# MAGIC 
# MAGIC ## Detecting AgentTeslaRAT with Databricks
# MAGIC Using the notebooks on this solution accelerator, you will be able to detect the Agent Tesla RAT. You will be using analytics for domain generation algorithms (DGA), typosquatting and threat intel enrichments from URLhaus. Along the way you will learn the Databricks concepts of:
# MAGIC 
# MAGIC * Data ingestion
# MAGIC * Ad hoc analytics
# MAGIC * How to enrich event data, such as DNS queries
# MAGIC * Model building and
# MAGIC * Batch and Streaming analytics
# MAGIC 
# MAGIC Why use Databricks for this? Because the hardest thing about security analytics aren’t the analytics. You already know that analyzing large scale DNS traffic logs is complicated. Colleagues in the security community tell us that the challenges fall into three categories:
# MAGIC 
# MAGIC ## Deployment complexity
# MAGIC DNS server data is everywhere. Cloud, hybrid, and multi-cloud deployments make it challenging to collect the data, have a single data store and run analytics consistently across the entire deployment.
# MAGIC Tech limitations: Legacy SIEM and log aggregation solutions can’t scale to cloud data volumes for storage, analytics or ML/AI workloads. Especially, when it comes to joining data like threat intel enrichments.
# MAGIC Cost: SIEMs or log aggregation systems charge by volume of data ingest. With so much data SIEM/log licensing and hardware requirements make DNS analytics cost prohibitive. And moving data from one cloud service provider to another is also costly and time consuming. The hardware pre-commit in the cloud or the expense of physical hardware on-prem are all deterrents for security teams.
# MAGIC In order to address these issues, security teams need a real-time data analytics platform that can handle cloud-scale, analyze data wherever it is, natively support streaming and batch analytics and, have collaborative, content development capabilities. And… if someone could make this entire system elastic to prevent hardware commits… now wouldn’t that be cool!
# MAGIC 
# MAGIC You can use this notebook in the Databricks community edition or in your own Databricks deployment. There are lot of lines here but the high level flow is this:
# MAGIC 
# MAGIC * Read passive DNS data from AWS S3 bucket
# MAGIC * Specify the schema for DNS and load the data into Delta
# MAGIC * Explore the data with string matches
# MAGIC * Build the DGA detection model. Build the typosquatting model.
# MAGIC * Enrich the output of the DGA and typosquatting with threat intel from URLhaus
# MAGIC * Run the analytics and detect the AgentTesla RAT
# MAGIC 
# MAGIC <img src='https://www.databricks.com/wp-content/uploads/2020/10/blog-detecting-criminals-2.png'>
# MAGIC 
# MAGIC ## Getting started
# MAGIC 
# MAGIC Although specific solutions can be downloaded as .dbc archives from our websites, we recommend cloning these repositories onto your databricks environment. Not only will you get access to latest code, but you will be part of a community of experts driving industry best practices and re-usable solutions, influencing our respective industries. 
# MAGIC 
# MAGIC <img width="500" alt="add_repo" src="https://user-images.githubusercontent.com/4445837/177207338-65135b10-8ccc-4d17-be21-09416c861a76.png">
# MAGIC 
# MAGIC To start using a solution accelerator in Databricks simply follow these steps: 
# MAGIC 
# MAGIC 1. Clone solution accelerator repository in Databricks using [Databricks Repos](https://www.databricks.com/product/repos)
# MAGIC 2. Attach the `RUNME` notebook to any cluster and execute the notebook via Run-All. A multi-step-job describing the accelerator pipeline will be created, and the link will be provided. The job configuration is written in the RUNME notebook in json format. 
# MAGIC 3. Execute the multi-step-job to see how the pipeline runs. 
# MAGIC 4. You might want to modify the samples in the solution accelerator to your need, collaborate with other users and run the code samples against your own data. To do so start by changing the Git remote of your repository  to your organization’s repository vs using our samples repository (learn more). You can now commit and push code, collaborate with other user’s via Git and follow your organization’s processes for code development.
# MAGIC 
# MAGIC The cost associated with running the accelerator is the user's responsibility.
# MAGIC 
# MAGIC 
# MAGIC ## Project support 
# MAGIC 
# MAGIC Please note the code in this project is provided for your exploration only, and are not formally supported by Databricks with Service Level Agreements (SLAs). They are provided AS-IS and we do not make any guarantees of any kind. Please do not submit a support ticket relating to any issues arising from the use of these projects. The source in this project is provided subject to the Databricks [License](./LICENSE). All included or referenced third party libraries are subject to the licenses set forth below.
# MAGIC 
# MAGIC Any issues discovered through the use of this project should be filed as GitHub Issues on the Repo. They will be reviewed as time permits, but there are no formal SLAs for support. 
