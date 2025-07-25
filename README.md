# Bigram Parser

A parsing utility that given some text will output bigrams and their counts.

---

## Prerequisites

- Python 3.x
- `pip` for installing packages
- (Optional) virtual environment such as `venv`

## Setup

1. **Clone the repository**

```bash
git clone https://github.com/dan-greenberg/bigram
cd bigram
```

2. **(Optional) Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## Running

You can run the code with either a file input or text from the command line.

### File input
```bash
$ ./bigram.sh -f path/to/input.txt
```

### Text input
```bash
$ ./bigram.sh -t "This is an example input."
```

### Example
```bash
$ ./bigram.sh -t "The quick brown fox and the quick blue hare."
"the quick": 2
"quick brown": 1
"brown fox": 1
"fox and": 1
"and the": 1
"quick blue": 1
"blue hare": 1
```

## Run Tests

Tests are run with pytest.

```bash
$ pytest
```

