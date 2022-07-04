# Technology
I have used the following language and tools majorly in the creation of this automation framework:
- [python (3.10.4)] (Used for scripting for instance calling request to server, using the response for different purposes and assertions etc.)
- [PyCharm (22.1.1)] (The IDE on which all the framework was created)
- [Git (2.36.1)] (For making codebase accessible online, for committing and pushing the code to automation repository, and for maintaining code versioning etc.)

# Why Python?
I have chosen python as a scripting language over other programming languages for the following reasons:
- Easy to Understand and use
- Python was mentioned as the preferred language in the assessment
- I have good hands-on experience of creating automation framework using python

# BDD Approach
Behavior Driven Development (BDD) approach was used while creating automation framework because of the following reasons:
- Easy adaptability and understanding about the test scenario 
- Common understanding among all the stakeholders in terms of test coverage
- Easy maintenance and usability

# Setup and Configuration
In order to make sure that the framework is up and running and the scenario(s) are getting executed without any hassle, some libraries and plugin are needed to be installed along with some configurations in the IDE itself. 
### Libraries
Following are the libraries that are needed to be installed for this purpose:
- pytest (Python framework for automation)
- pytest-bdd (pytest extension to support BDD approach)
- pyyaml (to support configuration related operations)
- selenium (python library that helps in interacting with browser in order to support UI automation)
- pytest-html (to view the test execution results in the form of informative reporting)

To install aforementioned libraries, one just need to install the following command in the PyCharm terminal:
```
pip install <library_name>
For e.g. pip install pytest
```
For further ease, I have already created the **requirements.txt** file under the project root directory. This file already contains all the libraries that are needed to run this framework. One simply can run the following command in the terminal and all the libraries will be installed at once:
```
pip install -r requirements.txt
```
### Plugins
For smooth setup of the automation framework under discussion, following are the plugins that can be added in the IDE:

- CMD Support (For smooth usage of CLI related operations)
- Gherkin (To get a clear view of different keywords used in the feature file)

One can simply go to the following path in the PyCharm, search for the above-mentioned plugin(s) and then can click on **Install**  button to simply add it:
```
File > Settings > Plugins > MarketPlace
```
**Note:** Restarting of IDE maybe required in order to make the plugins fully functional to the project.
### Configuration 
In order to complete the setup of the framework, couple of following configuration related changes are also needed to be performed:
- Setting up **base python interpreter** (File > Settings > Project:<project_name> (qa-assessment in this case) > Python Interpreter)
- Setting up the default test runner to **pytest** (File > Settings > Tools > Python Integrated Tools > Default test runner)

Once the setup gets completed, one can simply type the following command in the PyCharm terminal to get all the codebase of this automation framework:
```
git clone <url_of_automation_repo>
```
# Project Structure
The complete automation framework is being divided into the following 4 components:
- Drivers
- Features
- Reports
- Configurations
- Requirements Installation

### Drivers 
drivers is the first directory under the root folder which contains the WebDrivers, that are needed in order to execute the test cases on a particular browser. For now, Chrome and Edge WebDrivers are available. Rest can be added as well and can work fine with very minor tweak in the business logic file. Moreover, to execute these cases on any other platform like linux, MAC, one simply needs to download the driver of the respective platform and place it in this directory, it will start working on the particular environment


**Note:** Both the Chrome and Edge WebDrivers will support till 103.x version of the browser (since as of date these are the latest ones)
### Features 
features is the main directory under the root folder which contains the actual code including the business logic as well as the locators, feature file containing the test scenario(s) and the step definition file(s). Brief explanation of each component under features directory is given below:
##### Logic Directory
logic directory actually contains all the business logic needed to complete the qa-assessment. It contains the following folders/files:
- ui > pages > login > qa_assessment_utils.py (This file contains the business logic of the methods called from the user from step definition file like opening browser, sending login credentials, verifying some content etc.)
- ui > pages > login > qa_assessment_locators.py (This file contains the locators that were needed in order to complete the assessment)

##### Tests Directory
test directory contains the actual test scenario(s) to be executed in the feature file and the binding definition against each test statement in the step definition file. It contains the following folders/files:
- ui > login > qa_assessment.feature (This file contains the actual test scenarios in the Gherkin format which need to be executed in order to complete the qa-assessment)
- ui > login > test_qa_assessment_steps.py (It is actually the file that binds each test statement in the feature file (defined against Given, When, Then) to the actual code implemented behind the scenes. This file just calls the method, no business logic is defined here)

### Reports
To visualize the test execution results and details, reporting is very important aspect in any automation framework and this reports section serves the purpose. After each test execution, the html report(s) will be available under this directory to provide the test execution details such as its pass or fail state, execution time etc. To view the detailed logs about the execution, one can simply click on the **show details** link available under **Result** cell.

### Config.yml
Making framework configurable is really important since it test execution may be performed on different environments containing different URLs and credentials.Config.yml is the file which is used to store different set of configurations in it on the basis of environments and user just has to change a variable value against **execution_environment** key to use the configurations of the respective environment.

### Requirements.txt
This file is related to the setup of the framework and it contains all the libraries needed to be installed in order to run the framework smoothly.  One can simply add any other library if needed in the future in this file and can run this file through terminal which will install all the libraries at once.

# Execute Test(s)
The last stage is to execute the test scenario(s) from the framework in order to achieve the task completion goal. There are two ways to execute test scenario:
- Through PyCharm GUI
- Through Terminal

### PyCharm GUI
One can simply select the **run** icon against each test scenario (to execute single scenario) or can simply right-click in the step definition file to select **run** option to execute the whole step definition file. Just one thing that is needed to be kept in mind in this case is that the **Working Directory Path** in the configurations should be set to the **Root Directory Path** (10Pearls_assessment in our case) to execute the test(s) without any issue.
Moreover, user can provide **--html=reports/automation_report.html** under the **Additional Arguments** field in the configuration file to get the report of the test execution.
###  PyCharm Terminal
User can also execute the test(s) by providing the pytest run command(s) in the IDE terminal straightaway. 
In order to execute the complete step definition file containing one or multiple test scenarios along with the generation of the HTML report under reports directory, following command can be used:
```
pytest features\tests\ui\login\test_qa_assessment_steps.py --html=reports\automation_report.html
```
For the user to run any set of scenario(s) from the feature file, following command can be used
```
pytest -m=10pearls --html=reports\automation_report.html
 ```
Where **10pearls** is the tag that is being used in the feature file against test scenario. All the scenarios containing this tag will be executed with the above-mentioned command.

   [python (3.10.4)]: <https://www.python.org/downloads/>
   [PyCharm (22.1.1)]: <https://www.jetbrains.com/pycharm/download/#section=windows>
   [Git (2.36.1)]: <https://git-scm.com/downloads>