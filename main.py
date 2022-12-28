import config
import scraper
import applicator
import error_handler
import logger

def main():
    # Load the configuration settings
    settings = config.load_settings()

    # Set up the logger
    logger.setup_logger()

    try:
        # Scrape the job listings
        job_listings = scraper.scrape_jobs(settings)

        # Apply to the job listings
        applicator.apply_to_jobs(job_listings, settings)
    except Exception as e:
        # Handle the error
        error_handler.handle_error(e)

if __name__ == '__main__':
    main()
