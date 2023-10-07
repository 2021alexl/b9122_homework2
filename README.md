# b9122_homework2

### Tasks
## 1. United Nations Press Releases
Objective: Extract at least 10 press releases from the United Nations website that contain the word "crisis".

Seed URL: https://press.un.org/en

Criteria:

Press release pages have the "PRESS RELEASE" relative link in the top left corner.
The anchor tag for identifying press releases is: <a href="/en/press-release" hreflang="en">Press Release</a>

## 2. European Parliament Press Releases
Objective: Extract at least 10 press releases from the European Parliament's press room that cover plenary sessions and contain the word "crisis".

Seed URL: https://www.europarl.europa.eu/news/en/press-room

Criteria:

Press releases related to plenary sessions contain the text “PLENARY SESSIONS”.
The HTML tag for identifying plenary sessions is: <span class="ep_name">Plenary session</span>

### About the Author
Alex (Ke) Lan

Position: Data Science Co-op at Novo Nordisk

Education: MSBA at Columbia University | Economics & Statistics at Boston University

Email: kl3411@columbia.edu

Phone: 857-316-5572

Portfolio: alex-lan.webflow.io

LinkedIn: Ke Alex Lan


### Function Descriptions

1. is_press_release(soup)
Description: Checks if a given webpage (parsed with BeautifulSoup) is a press release page.

Parameters:

soup: A BeautifulSoup object containing the parsed content of a webpage.
Returns:

True if the page is a press release, False otherwise.
2. is_plenary_session(soup)
Description: Checks if a given webpage (parsed with BeautifulSoup) is related to "PLENARY SESSIONS".

Parameters:

soup: A BeautifulSoup object containing the parsed content of a webpage.
Returns:

True if the page is related to plenary sessions, False otherwise.
3. contains_crisis(soup)
Description: Checks if a given webpage (parsed with BeautifulSoup) contains the word "crisis".

Parameters:

soup: A BeautifulSoup object containing the parsed content of a webpage.
Returns:

True if the page contains the word "crisis", False otherwise.
4. add_link(link, visited, q)
Description: Adds a new link to the list of URLs to visit.

Parameters:

link: The link to be added.
visited: A set of URLs that have already been visited.
q: The query parameter indicating the type of press release to search for.
Returns:

The new link if it's valid and hasn't been visited, None otherwise.
5. find_press_release(url, visited, q)
Description: Finds press release links from a given URL based on the specified query.

Parameters:

url: The URL to search for press releases.
visited: A set of URLs that have already been visited.
q: The query parameter indicating the type of press release to search for.
Returns:

The press release link if found, and a list of new links to visit.
6. get_press_releases(seed_url, q)
Description: Retrieves press releases from a given seed URL based on the specified query.

Parameters:

seed_url: The starting URL to begin the search.
q: The query parameter indicating the type of press release to search for.
Returns:

A list of press release URLs that match the criteria.
