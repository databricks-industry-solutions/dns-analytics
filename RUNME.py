# Databricks notebook source
# MAGIC %md This notebook sets up the companion cluster(s) to run the solution accelerator. It also creates the Workflow to create a Workflow DAG and illustrate the order of execution. Feel free to interactively run notebooks with the cluster or to run the Workflow to see how this solution accelerator executes. Happy exploring!
# MAGIC 
# MAGIC The pipelines, workflows and clusters created in this script are user-specific, so you can alter the workflow and cluster via UI without affecting other users. Running this script again after modification resets them.
# MAGIC 
# MAGIC **Note**: If the job execution fails, please confirm that you have set up other environment dependencies as specified in the accelerator notebooks. Accelerators sometimes require the user to set up additional cloud infra or data access, for instance. 

# COMMAND ----------

# DBTITLE 0,Install util packages
# MAGIC %pip install git+https://github.com/databricks-academy/dbacademy-rest git+https://github.com/databricks-academy/dbacademy-gems git+https://github.com/databricks-industry-solutions/notebook-solution-companion

# COMMAND ----------

from solacc.companion import NotebookSolutionCompanion

# COMMAND ----------

job_json = {
        "timeout_seconds": 14400,
        "max_concurrent_runs": 1,
        "tags": {
            "usage": "solacc_automation",
            "group": "SEC"
        },
        "tasks": [
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                     "notebook_path": f"00_Shared_Include"
                },
                "task_key": "dns_01"
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                     "notebook_path": f"01_DNS_Analytics_Ingest"
                },
                "task_key": "dns_02",
                "depends_on": [
                    {
                        "task_key": "dns_01"
                    }
                ]
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                     "notebook_path": f"02_DNS_Analytics_Enrichment"
                },
                "task_key": "dns_03",
                "depends_on": [
                    {
                        "task_key": "dns_02"
                    }
                ]
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                     "notebook_path": f"03_DNS_Analytics_Exploring_Data"
                },
                "task_key": "dns_04",
                "depends_on": [
                    {
                        "task_key": "dns_03"
                    }
                ]
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                     "notebook_path": f"04_DNS_Analytics_Data_Science"
                },
                "task_key": "dns_05",
                "depends_on": [
                    {
                        "task_key": "dns_04"
                    }
                ]
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                    "notebook_path": f"05_DNS_Analytics_Streaming"
                },
                "task_key": "dns_06",
                "depends_on": [
                    {
                        "task_key": "dns_05"
                    }
                ]
            },
            {
                "job_cluster_key": "dns_cluster",
                "notebook_task": {
                    "notebook_path": f"06_DNS_Analytics_ScoreDomain"
                },
                "task_key": "dns_07",
                "depends_on": [
                    {
                        "task_key": "dns_06"
                    }
                ]
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "dns_cluster",
                "new_cluster": {
                    "spark_version": "10.4.x-cpu-ml-scala2.12",
                "spark_conf": {
                    "spark.databricks.delta.formatCheck.enabled": "false"
                    },
                    "num_workers": 2,
                    "node_type_id": {"AWS": "i3.xlarge", "MSA": "Standard_D3_v2", "GCP": "n1-highmem-4"}, # different from standard API
                    "custom_tags": {
                        "usage": "solacc_automation"
                    },
                }
            }
        ]
    }


# COMMAND ----------

dbutils.widgets.dropdown("run_job", "False", ["True", "False"])
run_job = dbutils.widgets.get("run_job") == "True"
NotebookSolutionCompanion().deploy_compute(job_json, run_job=run_job)

# COMMAND ----------


