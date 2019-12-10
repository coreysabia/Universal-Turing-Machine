# Universal Turing Machine

`Please note: If you are not viewing this README.md file on the GitHub repo, it might be a good idea to do so` - since it is written in markdown, it is rendered in a much more human readable format at the following link: https://github.com/coreysabia/Universal-Turing-Machine/blob/develop/README.md

This README.md is currently intended for the instructor of the class that this was written for. The contents within this doccument and this GitHub Repo are not intended to be public, but will be pulic for the next few weeks to allow ease of grading and submission to the instructor of the contributors to this repo. If you are not the instructor, please ignore this repo.

## [Step 1] Initial Download(s)

To run the program as intended you will need to follow the instructions listed just below this text. Please ensure that you have met all of the requirements in this first step before moving on.

1. Clone this repository. It can be done in one of the following ways: 
  1. If you already have Git installed you run the following command `git clone https://github.com/coreysabia/universal-turing-machine`
  2. If you already have GitHub Desktop installed you can, on the GitHub website, navigate to the main page of the repository. Just above the folders and code (to the right), click the green button which says `Clone or Download` and the select `Open in Desktop` to clone the repository in GitHub Desktop. Follow the prompts in GitHub Desktop to complete the clone.
  3. Finally, you can install a .zip of the repository by following almost all the steps from the previous option. On the GitHub website, navigate to the main page of the repository. Just above the folders and code (to the right), click the green button which says `Clone or Download` and the select `Download Zip` to download the repository as a .zip file. If you followed this step, please take a minute to un-zip the repository.
2. Download and Install Docker. Go to: https://hub.docker.com/?overlay=onboarding and login. Next download and install Docker on your local machine. Follow all prompts and ensure that virtulization is enabled on your machine (Docker will tell you if it is not when you try to run it).

## [Step 2] Translating the Transitions

If you have not already done so, or if you do not wish to use the transitions set that you provided the class `NOTE: the testing transitions that you provided the class are already translated and can be either used for the UTM or used as and example of how to properly translate new transitions. They can be found in the transitions/testing_transitions.json file inside this repository` please follow the instructions just below to translate the transitions you wish to use into the required json format. Please ensure you have met all of the requirements of this second step before moving on.

1. 

## [Step 3] Initial Setup

Now that you have downloaded and installed everything you need, and translated any transitions you wish to use it is time to make sure everything is setup and ready to go. Please ensure you have met all of the requirements of this third step before moving on.

1. Start Docker. Click on the Docker icon on your Desktop or wherever you put it, to run the Docker Desktop agent. Please wait 1 to 3 minutes for the Docker agent to fully boot.
2. Open a Command Line Interface (CLI). Since you are using windows, CMD will work perfectly.
3. On the CLI, navigate to the root directory of the repository that you either cloned or downloaded from GitHub using the `cd` and/or `dir` commands to navigate. Once you are in the root directory of the repository ensure that the file structure looks similar to the following:

├───.github/
│   └───workflows/
│       └───config.yml
├───src/
│   ├───__init__.py
│   ├───render.py
│   ├───test.py
│   ├───test2.py
│   ├───utils.py
│   └───utm.py
├───transitions/
│   ├───example_json_multiple.txt
│   ├───example_json_single.txt
│   ├───example_multi.json
│   ├───example_palindrome.json
│   ├───example_transitions.json
│   ├───testing_transitions.json
│   └───testing_transitions_copy.json
├───.gitignore
├───Dockerfile
├───Pipfile
├───Pipfile.lock
├───README.md
├───requirements.txt
└───run.py

4. Now that you are in the root directory of the repository, please run `docker build -t utm .` in the CLI to build the Docker image. (NOTE: Please ensure that you include the `.` (period) character when running the command.)
5. Once the Docker image has been built successfully (NOTE: this may take a few minutes the first time since it is gathering all the dependencies), you are able to now start the Docker container get a shell inside it. Do this by running `docker run -it utm:latest sh`. You should now see a `#` in your CLI indicating that you are now using the shell inside the running Docker container.

## [Step 4] Running the Universal Turing Machine (inside the Docker container)

Now that you have completed all of the previous steps you are finally ready to run the UTM. Please follow the instructions below in order to ensure that it is run correctly.

1. Start the UTM program by running the command `python run.py`.
2. You should now see the prompt: `? Enter the input tape:`. Please type or paste in the input tape now, and then click enter/return.
3. You should now see the prompt: `? Enter the path to the transitions file:`. Please enter the relative path to the transitions file which should be in the /transitions folder (NOTE: if you followed the instructions in [Step 4] you should have placed the file you created in this folder). If you are using the previously translated testing transitions that you provided the class, you should type or copy and paste in `transitions/testing_transitions.json`. (!!!PLEASE NOTE: Please ensure that the slash used is a single forward slash `/` since this is linux based Docker container.)
4. You should now see the prompt `? Enter the start state (default: q0): q0`. Please enter the starting state for the transitions if the starting state is not `q0` (NOTE: Please ensure to first delete the default input if you are not using `q0` before typing in a new value). (!!!PLEASE NOTE: If you are using the previously translated testing transitions that you provided the class, you should use `q1` here since that is the starting state that you provided)
5. You should now see the prompt `? Enter the final state (default: qdone):  qdone`. Please enter the final state for the transitions if the final state is not `qdone` NOTE: Please ensure to first delete the default input if you are not using `qdone` before typing in a new value). (!!!PLEASE NOTE: If you are using the previously translated testing transitions that you provided the class, you should use `q2` here since that is the ending state that you provided)
6. You should now see the prompt `? Enter the character for end markings/padding:`. 


### If you do not already have a python enviroment installed, start here.
1. Start by installing `Python 3.7`
2. Make sure Python is in your PATH (if on windows)
3. Update pip by running `python -m pip install --upgrade pip`.
4. Install pipenv by running `pip install pipenv`
5. Then follow list below.

### To build the local python enviroment with pipenv, start here.
1. Start by building pipenv files off of `requirements.txt` by running `pipenv update`.

## Running the UTM (Then do this)
1. Make sure you are in your local python enviroment by running `pipenv shell`.
2. Then make sure you are in the main directory where the file `run.py` is.
3. Finally, run one of the following commands, depending on what OS you are on.
### For unix:
`./run.py`
### For windows:
`python run.py`

### Docker:
1. docker build -t utm . 
2. docker run -it utm:latest sh 



### Examples and Explanation

Assumptions: Initial state is q0 and final state is qdone (you can define these when running the program)

```json
{
    "q0": {
        " ": {
            "write": "a",
            "move": "right",
            "nextState": "q1"
        }
    },
    "q1": {
        " ": {
            "write": "b",
            "move": "left",
            "nextState": "q1"
        },
        "a": {
            "write": "b",
            "move": "left",
            "nextState": "qdone"
        }
    }
}
```