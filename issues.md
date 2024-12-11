cannot import json from itsdangerous
pip install itsdangerous==2.0.1
pip install werkzeug==2.0.3
pip install jinja2==3.0.3 --force-reinstall

pip install itsdangerous==2.0.1 werkzeug==2.0.3 jinja2==3.0.3 --force-reinstall


    volumes:
      - /app/node_modules
      - ./frontend/src:/app/src

   volumes:
      - /app/node_modules
      - ./api:/app