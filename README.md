## Installation
1. Create a virutual environment
    ~~~
    python -m venv venv
    ~~~
2. Activate the virtual environment
   ~~~
   source venv/bin/activate
   ~~~
4. Install dependencies. You need to be carefull to add `-Wno-deprecated-declarations` and `-fcommon` C flags when
you install the dependencies.
   ~~~
   CFLAGS="-Wno-deprecated-declarations -fcommon" pip install -r requirements.txt
   ~~~