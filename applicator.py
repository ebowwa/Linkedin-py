import requests
import json

def apply_to_jobs(config, job_list):
    # Read the LinkedIn login credentials from the config file
    username = config['login']['username']
    password = config['login']['password']

    # Read the application materials and contact information from the config file
    resume = config['application']['resume']
    cover_letter = config['application']['cover_letter']
    phone = config['application']['phone']
    email = config['application']['email']

    # Iterate through the job listings and apply to each one
    for listing in job_list:
        job_id = listing['id']
        job_url = listing['url']

        # Set up the LinkedIn API request
        headers = {
            'X-Restli-Protocol-Version': '2.0.0',
        }
        data = {
            'jobId': job_id,
            'resume': resume,
            'coverLetter': cover_letter,
            'phone': phone,
            'email': email,
        }
        url = f'{job_url}/apply'

        # Send the request to the LinkedIn API
        response = requests.post(url, json=data, headers=headers)

        # Parse the response from the LinkedIn API
        result = json.loads(response.text)

        # Print the result of the application submission
        if result['success']:
            print(f'Successfully applied to job {job_id} at {listing["company_name"]}')
        else:
            print(f'Failed to apply to job {job_id} at {listing["company_name"]}')
                    # Print the result of the application submission
        if result['success']:
            print(f'Successfully applied to job {job_id} at {listing["company_name"]}')
        else:
            print(f'Failed to apply to job {job_id} at {listing["company_name"]}')

# Example usage of the apply_to_jobs() function
if __name__ == '__main__':
    # Read the configuration file
    with open('config.txt') as f:
        config = json.load(f)

    # Scrape the job listings
    job_list = scrape_jobs(config)

    # Apply to the job listings
    apply_to_jobs(config, job_list)

