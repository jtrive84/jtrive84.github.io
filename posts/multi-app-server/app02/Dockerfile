FROM rocker/shiny:latest

# Install additional R packages.
RUN install2.r --error data.table foreach

# Copy app code to the Docker image.
COPY app.R /srv/shiny-server/

# Change permissions for shiny app.
RUN chown -R shiny:shiny /srv/shiny-server

EXPOSE 3838

CMD ["/usr/bin/shiny-server"]
