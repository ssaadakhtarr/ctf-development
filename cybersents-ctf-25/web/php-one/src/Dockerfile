FROM php:apache

WORKDIR /var/www/html
COPY index.php .
COPY page/ page/
COPY flag.txt .

RUN mv flag.txt /flag_$(head /dev/urandom | tr -dc A-Za-z0-9 | head -c 23).txt

RUN chmod -R 755 /var/www/html && chmod 444 /flag_*.txt

EXPOSE 80

CMD ["apache2-foreground"]
