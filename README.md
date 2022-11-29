## <div id = "toc">Table of Contents</div>

- [Overview](#overview)
- [Examples](#examples)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Components Explanation](#components)
- [Releases](#releases)
- [Way to Feedback](#feedback)
- [How to Contribution](#contribution)
- [Key Collaborators](#collaborators)
- [License](#license)
- [Code of Conduct](#coc)

## <div id = "overview">Voca Test Generator</div>

When learning some foreign languages such as English, Japanese, and Chinese, memorizing the words is fundamentally required. Learners often check whether they have memorized completely through tests.

However, it is unnecessary for learners to spend time generating test papers one by one. Also, even if the test paper is made, testing with the same paper every time can be a meaningless test.

Therefore, we intend to provide a foreign language word memorization test paper that can be used by anyone through this application.

## <div id = "examples">Examples</div>

> need to upload some frontend screenshots

## <div id = "quick-start">Quick Start</div>

You can just access [Out Website](http://ec2-3-36-4-131.ap-northeast-2.compute.amazonaws.com:8080/).
> need to add some user scenarios.

## <div id = "installation">Installation</div>

Just Access [Our Website](http://ec2-3-36-4-131.ap-northeast-2.compute.amazonaws.com:8080/)!
If you want to run server in local, follow the instructions below.

1. Clone Project

    ```bash
    git clone https://github.com/jmhee28/Voca-testgenerator.git
    ```
2. Install Dependencies

    ```bash
    pip install -r requirements.txt
    ```
3. Run Server

    ```bash
    python manage.py runserver
    ```
4. Explore Website

    http://localhost:8000

## <div id = "components">Components</div>

> need to add other logic parts

### Dataset
In `dataset/` directory, there are some static foreign language words with korean meaning.

Each dataset file should be `.csv` format, which is comma-separated values. First value is for a foreign language word, and second value is a set of korean meanings of the first value.

- English
	- Elementary School Level
	- Middle School Level
	- TOEIC Level
	- TOFEL Level
- Japanese
- Chinese
- Classic Chinese

Our server uses these datasets to provide a test.

### Parser

The `Parser` module is responsible for parsing the dataset robustly. For any foreign languages, parser should provide pairs of (word, meanings). They can be used for making a new test paper for the users.

This module use regular expressions to parse appropriate values. Because a `word` value must be single word, the parts for parsing `word` check this requirement. In constrst, `meanings` value may be a set of Korean. The parts for parsing `meanings` split them to each meaning and make a list. In here, we assume that delimitters of `meanings` is one of `,`, `|`, `;`.

## <div id = "releases">Releases</div>

> need to list release versions

## <div id = "feedback">Feedback</div>

There are many ways in which you can give feedback in this application.

- Ask a question
- Report a bug
- Request a new feature
- Vote potential feature requests

## <div id = "contribution">Contribution</div>

There are many ways in which you can contribute in this application.

- Report bugs or Request a new feature by [making new issues](https://github.com/jmhee28/Voca-testgenerator/issues).
- Review source code changes in [pull requests](https://github.com/jmhee28/Voca-testgenerator/pulls).
- Provide new sets of foreign language words and [make pull requests](https://github.com/jmhee28/Voca-testgenerator/pulls).
- Review or translate documentation and [make pull requests](https://github.com/jmhee28/Voca-testgenerator/pulls).

## <div id = "collaborators">Key Collaborators</div>
| Name |        Email         |                    GitHub ID                    |                   Role                   |
|:----:|:--------------------:|:-----------------------------------------------:|:----------------------------------------:|
| 김경현  | woeiru12@g.skku.edu  |   [woeiru1006](https://github.com/woeiru1006)   |      Design UI and Develop Frontend      |
| 박승호  | tmdgh0221@g.skku.edu | [joonparkhere](https://github.com/joonparkhere) | Collect Datasets and Develop Data Parser |
| 정명희  | jmhee3410@g.skku.edu |      [jmhee28](https://github.com/jmhee28)      |        Develop Backend and Deploy        |

## <div id = "license">License</div>

Licensed under [MIT](https://opensource.org/licenses/MIT).

## <div id = "coc">Code of Conduct</div>

As a contributor, you can help us keep our application open and inclusive. Please read and follow our [Code of Conduct](CODE_OF_CONDUCT).
