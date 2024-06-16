# Projekt Aplikacje internetowe w Django


1. Przejście do root projektu

    ```bash
    cd <dir projektu>
    ```

2. Zbudowanie obrazu docker

    ```bash
    docker-compose up -d --build
    ```

3. Migracja bazy dabych

    ```bash
    docker exec -it <id-kontenera> bash -c "python manage.py migrate"
    ```

4. Otwarcie apliakcji

    - [http://localhost:8000](http://localhost:8000)
    - [http://localhost:80](http://localhost:80) - po reversed proxy
