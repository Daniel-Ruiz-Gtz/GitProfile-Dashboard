# GitProfile Dashboard

GitProfile Dashboard is a simple GUI application built with Tkinter that allows users to view GitHub user profiles. It retrieves data from the GitHub API and presents it in a user-friendly interface.

## Features

- View user details such as username, followers, following, bio, company, location, and email.
- Click on the username to open the user's GitHub profile in a web browser.
- Handle cases where the GitHub user is not found with a user-friendly error message.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- `ttkbootstrap` library
- `requests` library
- `Pillow` library (PIL)
- Python 3.x

You can install the dependencies using the following command:

```bash
pip install ttkbootstrap requests Pillow
```

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/Daniel-Ruiz-Gtz/GitProfile-Dashboard.git
cd GitProfile-Dashboard
```

2. Run the application:

```bash
python main.py
```

3. Enter a GitHub username and click the "Search" button to view the user's profile.

## Screenshots

![Screenshot](https://github.com/Daniel-Ruiz-Gtz/GitProfile-Dashboard/blob/main/public/ss/01.png)
![Screenshot](https://github.com/Daniel-Ruiz-Gtz/GitProfile-Dashboard/blob/main/public/ss/02.png)
![Screenshot](https://github.com/Daniel-Ruiz-Gtz/GitProfile-Dashboard/blob/main/public/ss/03.png)

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/my-feature`.
3. Commit your changes: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature/my-feature`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [ttkbootstrap](https://github.com/TkinterEP/ttkbootstrap) for styling the Tkinter GUI components.
- GitHub API for providing user profile data.
