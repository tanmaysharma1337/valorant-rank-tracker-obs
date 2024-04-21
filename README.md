<h3 align="center">Valorant Rank Tracker for OBS</h3>
<p align="center">
A Realtime Valorant Rank tracker app to integrate with OBS
<br/>
<br/>
<br/>
<a href="https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS">View Demo .</a>  
<a href="https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/issues/new?labels=bug&template=bug-report---.md">Report Bug .</a>
<a href="https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
</p>
</div>

 ## About The Project

<p align="center">
  <img width="400px" src="https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/assets/159008441/4a5cbf18-fef2-4622-ab9f-329d24a91abe"/>
</p>
<p align="center">
  <img src="https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/assets/159008441/26059588-528a-459c-b42c-a3298bc82092"/>
</p>

Keep track of your Valorant ranks in real-time with this handy desktop overlay and OBS integration. Never miss a beat as you climb the ranks in Valorant with this convenient tool.

Features:

- Desktop Overlay: Display your Valorant rank directly on your desktop screen, ensuring you're always aware of your current standing without needing to switch windows.
- OBS Integration: Seamlessly integrate your Valorant rank into your OBS streams. Whether you're a content creator or just want to showcase your progress to your audience, this feature makes it easy to include your rank in your streams.
- Real-Time Updates: Stay up-to-date with your latest rank as the overlay and OBS integration automatically update in real-time, reflecting any changes as soon as they occur.
  
 ### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

- [Python](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html)
- [Pillow](https://pypi.org/project/pillow/)
  
 ## Getting Started

1. Download Git and Python - [Install Python](https://www.python.org/downloads/) [GIT](https://git-scm.com/downloads)
2. Clone the repo
   ```sh
   git clone https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS.git
   ```
3. Install Required packages
   ```sh
   pip install tk
   pip install PIL
   pip install pyinstaller
   ```
4. Go to the project directory in command prompt and type
   ```sh
   pyinstaller ValorantTracker.spec
   ```
5. Go to "dist" folder in your project folder and run ValorantTracker.exe to launch the tracker app
   
 ## Usage

You can use this tracker app as your usual desktop overlay to track your valorant rank or you can use it inside OBS to show an overlay of valorant rank over your stream
To set it as an overlay in your OBS follow these steps :-
- Inside OBS create a new window capture inside sources by clickin the plus(+) icon
- Run ValorantTracker.exe
- Inside the window capture property set target as ValorantTracker.exe
  
 ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
 ## License

Distributed under the MIT License. See [MIT License](https://opensource.org/licenses/MIT) for more information.
 ## Contact
Project Link: [https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/](https://github.com/tanmaysharma1337/valorant-rank-tracker-OBS/)
 ## Acknowledgments

This project uses a free and unofficial version of valorant rank API provided by kyroskoh , and i thank him for making that :)

- [kyroskoh's Github](https://github.com/kyroskoh)
