---
date:
  created: 2022-01-30
  updated: 2025-01-17
slug: welcome-to-vecko.me
---

# A new website, a new beginning. Welcome to vecko.me!

_EDIT: I've since released the vecko.me domain - back to good ol' GitHub pages URL._

!!! note "Update"

    This post is now out of date. I have since moved to a version using mkdocs. Surprise surprise - takes time to maintain something bespoke 🙂.

Ever since I started coding a few years ago, I have always loved doing personal projects to explore what is possible with computers, and to just straight up have fun. As I developed my coding skills, what started off as small games with bucket-loads of "if" statements turned into more mature, fully fledged projects.

As I was doing this, I came to encounter two problems:

- there wasn't an easy way for me to share my projects with others
- I don't do nearly enough projects as I would like to

So I present to you my website, the silver bullet for both of these problems! An easy way to share what I get up to and to discuss it with others, as well as a way for me to keep me motivated and accountable with projects (as my projects aren't just for my own entertainment any more).

Of course, the act of constructing this website has been a project in itself. In fact, it has been one of my biggest projects so far. Through doing this project, I have learned a lot about web development. In the following sections, I will go through my process of developing the website, as well as going over the choices I made. I won't be delving into the the code, but if that is your fancy, the whole project is [visible on GitHub](https://github.com/VeckoTheGecko/VeckoTheGecko.github.io) for you to check out.

# The implementation

## Static or dynamic

When designing a website, you need to first decide what type of website you are wanting to build. One of these decisions is whether you want your site to be static or dynamic.

A **dynamic** site is a site like Facebook, or Twitter. These websites are constantly changing as new people add content to the website, and everyone's experience on the website is different. Once I log into my account, my feed is tailored based on who I follow. For a dynamic site to function, there needs to be a server either serving me the tailored webpages (["server side rendering"](https://www.freecodecamp.org/news/what-exactly-is-client-side-rendering-and-hows-it-different-from-server-side-rendering-bd5c786b340d/)) or serving me the relevant data so that my browser can assemble the webpages itself (["client side rendering"](https://www.freecodecamp.org/news/what-exactly-is-client-side-rendering-and-hows-it-different-from-server-side-rendering-bd5c786b340d/)). Due to the servers and databases associated with dynamic websites, there is a cost associated with them that scales with the more users your website has.

A **static** site on the other hand doesn't offer a unique experience to its users. Every user gets served the same static webpages, and hence everyone gets the same experience.
Static websites can really just be written in plain HTML, CSS and JavaScript which is then displayed in the browser (this is how things were done in the early days of the internet), but this approach just isn't scalable. Ideally you would want to use an SSG (Static Site Generator) like [Hugo](https://gohugo.io/), [Jekyll](https://jekyllrb.com/), or [Gatsby](https://www.gatsbyjs.com/) which takes data, and structured text (like markdown documents) and use that to generate the individual pages for the website. This allows you to easily edit your data and files without having to dig through raw HTML. Every time you change the underlying data you would need to recompile the website.
As you only need a place to store the files, and a script to occasionally compile the site, the cost for a static website is minimal (on the order for $0.50 a month, or even for free if you use GitHub Pages).

From those descriptions, you'll probably agree with me that for a blog type website, a static website using a static site generator is ideal! I chose to use Hugo as an SSG for its speed, and its ease of setup.

## Working in Hugo

The beauty of working with an SSG is that since the content which is used to make the website, and the logic required to generate the website is separate, making it really easy to get up and running with a slick new website. By using a theme (which provides the website building logic to the SSG), you are able to set up a website quickly in less than 30 minutes. And the beauty is that there are a lot of freely available themes for different types of sites, allowing you to choose the theme that best suits your needs.
With everything going to plan, you can go from not having a website, to having a website that is accessible to the world for free in less than an hour.

However, I didn't take this quick approach. I couldn't find a theme for Hugo that I really liked, and I also wanted to have full control over how my website was built. So I decided to embark on the journey of creating my own custom theme.

When starting to learn how to develop in Hugo, I found this YouTube [playlist by Mike Dane](https://youtube.com/playlist?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) that provides a really good insight into Hugo. This was a good gateway into how to work with Hugo, but I found that the best thing was really to look at the source code of existing themes. By setting up a theme, and then looking through the source code and investigating how it works, you're able to learn a lot more that what can be covered in a YouTube playlist. You can draw inspiration from problems that the theme creators encountered, and how they went about solving it. By looking at the source code, you can pick and choose features that you think would be good for your site or (equally importantly) know which features you don't want to use.

## Making it beautiful

Hugo takes care of how the content gets assembled into the structure of the website (what goes on what page). Whats left is making the website look good (the colours, the fonts, the visual layout etc.). This is where CSS comes in. Something that I have learned from previous projects is that doing the styling of the website, it is much easier to mock it up first in design software before you dive into the code. Foregoing this intermediate step can lead you to spending 40 minutes centring an item just to realise it looks trash (...not talking from experience, I'm much better than that of course).

Figma came to the rescue again this time, and is a really good application for doing these mock ups. By sorting out the fonts, the visual layout, and the colour scheme beforehand, you are able to start the CSS with a clear goal in mind.

And that's what I did, I wrote the CSS to replicate my Figma design and all was good...or so I thought. One concept that that I completely neglected was responsiveness. Your design should be able to adapt so that it looks good on all devices. If this isn't done correctly, it can make a website unusable on mobile. That was my website, it was great on desktop, but terrible on mobile (items misaligned, and items flowing off the right side of the screen).

Making responsive designs just using CSS is quite challenging. At this point I remembered [Bootstrap](https://getbootstrap.com/) which is a CSS toolkit that comes pre-built with a lot of commonly used styles and components. The best part is that the styles and components can adapt based on what screen size you use. For me, this allowed me to size my elements correctly, cut down a lot of the unnecessary CSS code I had, as well as have the layout change as the screen size got smaller. Due to the sheer popularity of Bootstrap, I was also able to find examples of what I wanted, and then adapt them to my needs.

Finally, the finishing touch that I needed was a small amount of customisation of Bootstrap. Bootstrap is built using Sass, a compiler that allows you to programmatically generate CSS to include in your website. By including some custom Sass files, I was able to extend the functionality of Bootstrap by tweaking Bootstrap's colours and by adding a couple more buttons.

## Deployment

All of the files for the website are stored on GitHub in a repository. I have set up GitHub actions so that if I make changes to the source files in the `main` branch, they are taken and compiled into the public website files which are then stored in the separate branch `gh-pages`. This branch is then served to the world using GitHub pages.

And that's it! My whole website in a nutshell.

# Where from here

There is still room to improve the website. Besides the small changes that I will be making along the way, there are some features that I would like to add to the website. As of writing this, these are some of the features that are lacking and that I would like to include:

- Search engine optimisation
  - Google doesn't know I exist. Even though the website is readable for humans, its not that easy for a bot to crawl it.
- Comment support
  - With static websites, one would think that one wouldn't be able to comment on posts. However, there are creative ways of accomplishing it (eg. [Utteranc.es](https://utteranc.es/) or Disqus).
- Search support
  - When I have written some more posts, I would like to have posts be searchable from within the website.

For the moment though, I feel that I have spent enough energy developing the website, and its time that I get to writing interesting posts to go along with it. This will be my primary goal over the next months.
