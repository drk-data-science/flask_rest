# flask_rest
you need to either have .env file in your directory which you source or export these settings

## for dev

```bash
source activate bucketlist
export FLASK_APP="start.py"
export SECRET="sdlkjdlkldsfkjdflkjdfslkjsldkjdlkjsdlkjsdfklj"
export APP_SETTINGS="development"
export DATABASE_URL="sqlite:///flask_rest.db"
```

## for testing

```bash
source activate bucketlist
export FLASK_APP="start.py"
export SECRET="sdlkjdlkldsfkjdflkjdfslkjsldkjdlkjsdlkjsdfklj"
export APP_SETTINGS="testing"
export TEST_DATABASE_URL="sqlite:///test/test_flask_rest.db"
```

to test
```bash
py.test
```
