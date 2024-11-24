# ML-Cirrhosis-Project

## Problem Statement
 
Cirrhosis results from prolonged liver damage, leading to extensive scarring, often due to conditions like hepatitis or chronic alcohol consumption. This required traditional methods to diagnos liver diseases such as biopsies or imaging. But with Machine Learning algorithms(Gradient Boost, SVM, RandomForest...) and tools we can analyze complex patterns and relationships to predict whether a person have liver disease. The [dataset](https://archive.ics.uci.edu/dataset/878/cirrhosis+patient+survival+prediction+dataset-1) is taken from uci.edu

## Data Features Information

1. ID: unique identifier
2. N_Days: number of days between registration and the earlier of death, transplantation, or study analysis time in July 1986
3. Status: status of the patient C (censored), CL (censored due to liver tx), or D (death)
4. Drug: type of drug D-penicillamine or placebo
5. Age: age in [days]
6. Sex: M (male) or F (female)
7. Ascites: presence of ascites N (No) or Y (Yes)
8. Hepatomegaly: presence of hepatomegaly N (No) or Y (Yes)
9. Spiders: presence of spiders N (No) or Y (Yes)
10. Edema: presence of edema N (no edema and no diuretic therapy for edema), S (edema present without diuretics, or edema resolved by diuretics), or Y (edema despite diuretic therapy)
11. Bilirubin: serum bilirubin in [mg/dl]
12. Cholesterol: serum cholesterol in [mg/dl]
13. Albumin: albumin in [gm/dl]
14. Copper: urine copper in [ug/day]
15. Alk_Phos: alkaline phosphatase in [U/liter]
16. SGOT: SGOT in [U/ml]
17. Triglycerides: triglicerides in [mg/dl]
18. Platelets: platelets per cubic [ml/1000]
19. Prothrombin: prothrombin time in seconds [s]
20. Stage: histologic stage of disease (1, 2, 3, or 4)

### Class Labels
Status: status of the patient 0 = D (death), 1 = C (censored), 2 = CL (censored due to liver transplantation)


## Local Setup
**Installation: Clone the repository** `git clone https://github.com/Hsinghsudwal/ml-project.git`

1. Set up Environment for managing libraries and running python scripts.
    install pipenv via cmd terminal if isn't install on your machine.
   ```bash
   pip install pipenv
   ```
2. **Activate environment**
   ```bash
   pipenv shell 
   ```
   This will create pipfile and pipfilelock within the environment.

3. **Initialize a New Pipenv Environment and Install Dependencies**:
   ```bash
   pipenv install 
   ```
   `pipenv install -r requirements.txt`
   
 

## Notebook
**Run Jupyter Notebook**:
From within Pipenv virtual environment, now can run the Notebook. On the terminal, from your main project directory to
```bash
   cd notebook
   jupyter lab
   ```
Perform EDA, Feature Engineering, Model Trainer and Model Evaluation. Also use Hypertuning technique such as GridSearchCV and Optuna. 

## Src
**Run Python Scripts**:
1. Save the working jupyter notebook to `src` directory once completed.
2. Convert jupyter notebook to script by

   `jupyter nbconvert --to script notebook.ipynb`

3. Once you edit your script, you can run python scripts within the pipenv virtual environment. For example, if you have a script named `train.py`, you can run it from your main project directory:  
   ```bash
   python src\train.py
   ```
This script will output the model to save into `output` and use in deployment

## Deployment
**Creating Docker image and Flask application**:

**Steps:** From the main project directory create `directory deployment`. Then `cd deployment`.
1. Create script to run flaskscript within the Pipenv virtual environment. When completed run via
   ```bash
   python predict.py
   ```

2. **Test APIs**: Create `test.py` to test the model contains a person_data. Pass this sample in new terminal
   ```bash
   python deploment\test.py
   ```
3. **DOCKER:** From the main project directory `cd deployment`.
* Create docker file for container!
   ```FROM python:3.11.5-slim
   RUN pip install pipenv
   WORKDIR /app                                                          
   COPY ["Pipfile", "Pipfile.lock", "./"]
   RUN pipenv install --system --deploy
   COPY ["predict.py", "best_model.pkl", "./"]
   EXPOSE 9696
   ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]
   ```
4. Docker -check image to see if docker is install and/or working on your machine
   ```bash
   docker images
   ```
4. Build Docker
   ```bash
   docker build -t project .
   ```
5. Running Docker 
   ```bash
   docker run -it --rm -p 9696:9696 project
   ```
   or detach running flag -d

   `docker run -it -d --rm -p 9696:9696 project`

6. **Test your API**:
    After running the container, on the main project directory contains `api.py` file. Which contains three different samples. you can un-comment or you can change the parameters to see the different results. By edit `api.py` or passing 

   ```bash
   python api.py
   ```
   **Using click recording and taken images of how to interact with the deployed service and see the result while the service is running vs container shut down which results error**

## Next Step
   - Try to deploy on cloud services like (aws, gcp...)
   - Monitor the model performance over time
   - Data monitor so that passed data is corect format such as (Float, Int, Str, bool)




   

