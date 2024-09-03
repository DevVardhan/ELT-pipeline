# End-to-End ELT Pipeline

## Pipeline Overview

This repository contains a data pipeline designed to automate the process of extracting data from a source database, loading it into a destination database, and then performing data transformations using dbt (data build tool).

## Key Features

- **Data Extraction**: Extracts data from a specified source database.
- **Data Loading**: Loads the extracted data into the destination database for further processing.
- **Data Transformation with dbt**: Utilizes dbt to transform the loaded data, ensuring it is optimized and ready for analysis.

## Workflow

1. **Extract**: The pipeline connects to the source database, extracts the necessary data, and prepares it for loading.
2. **Load**: The extracted data is then loaded into the destination database, setting the stage for transformation.
3. **Transform**: dbt is employed to transform the loaded data, applying necessary business logic and preparing the data for analytics or reporting.

## Technologies Used

- **Source Database**: [Specify Database Type, e.g., MySQL, PostgreSQL]
- **Destination Database**: [Specify Database Type, e.g., PostgreSQL, Redshift]
- **dbt**: For data transformation and modeling
- **Docker**: To containerize the environment for consistent and isolated execution.
- **Subprocess**: For running command-line processes programmatically within the pipeline.
- **Cron Job**: For scheduling and automating the pipeline execution at specified intervals.

## How to Run

### Prerequisites

- Ensure that Docker is installed and running on your system.
- Install `dbt` and configure it for the destination database.

### Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Configure the connection settings** for both the source and destination databases. Update the configuration files in the `config/` directory.

3. **Configure dbt**:
    ```bash
    pip install dbt-core dbt-postgres --user

4. **Build and run the Docker containers**:
    ```bash
    docker-compose up --build
    ```

5. **Run the pipeline**:
    - The pipeline can be executed manually using the command:
      ```bash
      python run_pipeline.py
      ```
    - Alternatively, you can set up a cron job to run the pipeline automatically at scheduled intervals. Example:
      ```bash
      0 0 * * * /usr/bin/python3 /path/to/your/repo/run_pipeline.py
      ```

6. **Stop the Docker containers and remove volumes**:
    ```bash
    docker-compose down -v
    ```

. **Monitor and review the transformation results**: Check the destination database for the transformed data, or review dbt logs and reports for more details.

## Documentation

 **Pipeline Configuration**: Detailed information about configuring the source and destination databases can be found in the `docs/configuration.md` file.
- **Running dbt**: Refer to the `docs/dbt.md` file for instructions on setting up and running dbt within the pipeline.
- **Docker Setup**: Instructions for setting up and troubleshooting Docker can be found in the `docs/docker.md` file.

## Tech Stack

- ![Docker](https://img.shields.io/badge/-Docker-2496ED?logo=docker&logoColor=white&style=flat-square) **Docker**: To containerize the application and ensure consistent environments.
- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) **Python**: For writing and managing the pipeline scripts.
- ![Subprocess](https://img.shields.io/badge/-Subprocess-4EAA25?logo=python&logoColor=white&style=flat-square) **Subprocess**: To manage the execution of command-line tools within the pipeline.
- ![SQL](https://img.shields.io/badge/-SQL-003B57?logo=postgresql&logoColor=white&style=flat-square) **SQL**: For querying and managing data within databases.
- ![Bash](https://img.shields.io/badge/-Bash-4EAA25?logo=gnu-bash&logoColor=white&style=flat-square) **Bash**: For scripting and automation tasks.
- ![Cron Job](https://img.shields.io/badge/-Cron_Job-002F56?logo=linux&logoColor=white&style=flat-square) **Cron Job**: To schedule automated execution of the pipeline.
- ![dbt](https://img.shields.io/badge/-dbt-FC4422?logo=dbt&logoColor=white&style=flat-square) **dbt**: For data transformation and modeling.



## Contact

For questions or support, please contact ME at ![email](devvardhan456@gmail.com).
