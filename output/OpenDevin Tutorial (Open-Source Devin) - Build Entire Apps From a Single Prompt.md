# Transcript: OpenDevin Tutorial (Open-Source Devin) - Build Entire Apps From a Single Prompt

[Watch Video](https://www.youtube.com/watch?v=dKD4a_sv69o&t=5s)

| Timestamp | Text |
|-----------|------|
| 00:00 | do you remember Devon that incredible |
| 00:01 | demo that we saw just a couple weeks ago |
| 00:04 | where you gave the agents a prompt and |
| 00:06 | they built out entire code bases and I |
| 00:08 | know we've seen stuff like that before |
| 00:10 | but what really set Devon apart was the |
| 00:13 | fact that it had this incredible |
| 00:14 | interface that included the terminal the |
| 00:16 | browser the code editor and all the |
| 00:18 | agent dialogue and it was really |
| 00:20 | impressive but it had one major flaw it |
| 00:22 | was completely closed source and not |
| 00:25 | more than a couple days after that demo |
| 00:27 | went viral now we have a completely open |
| 00:30 | source version of Devon called open |
| 00:32 | Devon and today I'm going to show it to |
| 00:35 | you and that's what you're looking at |
| 00:36 | right now so I'm going to show it to you |
| 00:38 | I'm going to show you how to use it and |
| 00:39 | I'm going to show you how to install it |
| 00:41 | so this is it and I already set it all |
| 00:43 | up so let me show it to you first so it |
| 00:45 | says hello I'm Devon and I asked it |
| 00:48 | write a simple calculator app with |
| 00:50 | python so it started writing a new task |
| 00:52 | here on the right side you can see the |
| 00:54 | terminal very akin to the original Devon |
| 00:57 | we have the planner over here we have a |
| 00:59 | code editor where you can actually see |
| 01:01 | all of the code and then we have the |
| 01:03 | browser over here you can select the |
| 01:05 | different models that you want to run so |
| 01:07 | right now it supports open Ai and Cloud |
| 01:09 | 3 but you can easily plug in an open |
| 01:11 | source local model as well and then over |
| 01:13 | here we have the browser and you can |
| 01:15 | choose between Lang chains agent and |
| 01:17 | code act agent and to be honest I don't |
| 01:20 | actually know the difference between |
| 01:21 | these two I haven't had a chance to test |
| 01:23 | code act agent so I'm using langing |
| 01:25 | chains agent but let's continue so |
| 01:28 | starting a new task then we go over to |
| 01:29 | the the terminal and we can actually see |
| 01:31 | so command LS there it is it looks where |
| 01:33 | it's at then it's reading from the |
| 01:36 | app.py it seems there's already a file |
| 01:39 | that does this it's a calculator app and |
| 01:41 | so on and so forth and you can see all |
| 01:42 | the output here it even tested it for me |
| 01:46 | which is really nice and then after all |
| 01:48 | that which really just took a few back |
| 01:50 | and forths and it's a very simple app |
| 01:52 | build a calculator app all done what's |
| 01:54 | next on the agenda I iterated on it so |
| 01:56 | now make an HTML interface for the |
| 01:59 | calculator so starting a new task and |
| 02:01 | then it went back and forth spun up |
| 02:03 | Local Host even tested it made sure it |
| 02:05 | all worked and then it was done so all |
| 02:07 | of this was actually pretty inexpensive |
| 02:10 | tokens wise um but it was really |
| 02:12 | impressive and you can run the |
| 02:13 | calculator like this so python |
| 02:15 | calculator. piy or you can spin up a |
| 02:18 | server and here's the calculator this is |
| 02:20 | what it built for me with just that |
| 02:22 | simple prompt so you put in your number |
| 02:24 | right here put in another number I'll |
| 02:26 | say four calculate very very basic but |
| 02:30 | the point is it works now I'm back at |
| 02:32 | open Devon and I am running it on Local |
| 02:35 | Host so this is running locally I am |
| 02:36 | using gp4 although I could easily swap |
| 02:40 | out an open source model which I'll show |
| 02:42 | you in a bit now the important thing to |
| 02:43 | remember is this project has not been |
| 02:45 | around long I'm talking days so there |
| 02:48 | are still some bugs some features still |
| 02:51 | don't work but it is very usable and the |
| 02:55 | rate of progression and new features |
| 02:58 | being added is super impressive |
| 03:00 | impressive so this is the project open |
| 03:02 | Devon it has over 8 and half thousand |
| 03:04 | stars already and if you look at GitHub |
| 03:07 | trending it is the number one trending |
| 03:09 | app on GitHub so this is going to grow |
| 03:12 | quickly and if I scroll down a little |
| 03:14 | bit there's another open source version |
| 03:16 | of Devon project called DEA although I |
| 03:18 | have tried every single day to get this |
| 03:20 | working and I can't so I'm going to keep |
| 03:22 | trying as soon as I can I'll make a |
| 03:24 | tutorial video for that but I am able to |
| 03:26 | get open Devon working and it works |
| 03:28 | really well so enough talk let me show |
| 03:31 | you how to install it I ran into a bunch |
| 03:33 | of issues hopefully I will show you how |
| 03:36 | to solve all of them and most of the |
| 03:38 | issues actually have nothing to do with |
| 03:40 | Devon they have to do with python |
| 03:42 | package management and environment |
| 03:43 | management which you know is the bane of |
| 03:46 | my existence so open a visual studio |
| 03:49 | code and that's where we're going to |
| 03:50 | start click on this button to toggle the |
| 03:52 | panel and we're going to open up our |
| 03:53 | terminal and what we're going to do is I |
| 03:55 | like to put stuff on my desktop when I'm |
| 03:57 | first playing around with it so we're |
| 03:58 | going to CD to the desktop now switch |
| 04:00 | back to the open Devon GitHub repository |
| 04:03 | you're going to click this green code |
| 04:05 | button right there and we're going to |
| 04:06 | copy the GitHub repo URL now we're going |
| 04:08 | to switch back to our terminal and we're |
| 04:10 | going to type get clone and then paste |
| 04:12 | in that URL and then hit enter and |
| 04:15 | that's it we've cloned it to our desktop |
| 04:17 | next we're going to CD into open Devon |
| 04:20 | and next we're going to click this |
| 04:22 | little button right here Explorer we're |
| 04:24 | going to open folder select the desktop |
| 04:26 | and then we're going to select open |
| 04:27 | Devon and now we have the open Deon |
| 04:29 | project open in Visual Studio code all |
| 04:32 | right now that we have that going let's |
| 04:34 | spin up a new cond environment so we're |
| 04:36 | going to do condac create DN o for open |
| 04:39 | Deon python equals 3.10 and we're going |
| 04:42 | to hit enter now I already have an |
| 04:43 | environment named that because I've gone |
| 04:45 | through this once to make sure it all |
| 04:46 | works before I show it to you so you're |
| 04:48 | not going to see this but go ahead and |
| 04:50 | install it just hit enter all right once |
| 04:52 | that's done we're going to grab this |
| 04:54 | Command right here cond to activate OD |
| 04:56 | copy paste it and it should say OD right |
| 04:58 | here it may not in your terminal if your |
| 05:01 | terminal structure is a little different |
| 05:02 | but for me I show it right there so |
| 05:04 | there we go we have o activated the next |
| 05:07 | thing you're going to need is Docker and |
| 05:09 | I'm really glad that they use Docker |
| 05:11 | because it makes the entire installation |
| 05:13 | much easier and you can actually run |
| 05:14 | these code environments in a completely |
| 05:17 | dockerized environment so to check if |
| 05:19 | you have Docker you're going to type |
| 05:20 | Docker PS and I do and there it is |
| 05:23 | however when you run Docker PS you might |
| 05:25 | get Docker is not recognized and if |
| 05:27 | that's the case you need to download |
| 05:28 | docker so you're going to come to docs. |
| 05:31 | do.com sengine install and you're going |
| 05:34 | to look for the docker desktop client |
| 05:36 | that matches your operating system so |
| 05:39 | I'm on a Mac so I click right there once |
| 05:41 | you do that it'll download and |
| 05:43 | everything else is really just drag and |
| 05:45 | drop or kind of clicking through an |
| 05:46 | interface it's very very easy you don't |
| 05:48 | need to do anything in console once |
| 05:50 | you're done with that open up vs code |
| 05:52 | again and you're going to type Docker PS |
| 05:55 | and now you should see at least this top |
| 05:57 | row right here container ID etc etc so |
| 06:00 | the next thing we're going to do is pull |
| 06:02 | the docker image and again this makes |
| 06:04 | everything really easy so we're going to |
| 06:05 | type Docker pull |
| 06:08 | gc. |
| 06:10 | iops sandbox colon |
| 06:13 | v0.1 and hit enter and there we go it's |
| 06:16 | 150 megabytes downloads quite quickly |
| 06:19 | extracts and we're done so that worked |
| 06:21 | perfectly okay next we need to export |
| 06:24 | our open AI API key so to start we're |
| 06:27 | going to use open AI but I'll show you |
| 06:29 | how to set up a local model towards the |
| 06:30 | end of the video so if you don't already |
| 06:33 | have an open AI account go ahead and |
| 06:35 | sign up you need a developer account |
| 06:36 | platform. |
| 06:38 | open.com ai- Keys you're going to click |
| 06:41 | create new secret key and I'm going to |
| 06:43 | type odop Devore YT so I know it's for |
| 06:48 | YouTube and I will revoke this key |
| 06:50 | before publishing this video click copy |
| 06:52 | go back and we're going to export it |
| 06:54 | just like that and then hit enter okay |
| 06:57 | now we've exported it and basically what |
| 06:59 | export it does is it saves it as an |
| 07:01 | environment variable that we can use |
| 07:02 | with this software however the better |
| 07:04 | way to do it is to actually create a EnV |
| 07:07 | file and store it there but I'll leave |
| 07:09 | that for you to do the next thing we |
| 07:11 | need to do is set our workspace |
| 07:12 | directory and so what I'm going to set |
| 07:14 | it as is export workspace Ford equals |
| 07:18 | squiggly line/ desktop slop Deon so I'm |
| 07:22 | going to keep the workspace in the open |
| 07:24 | Devon folder just to keep it all in one |
| 07:26 | place so go ahead and hit enter there |
| 07:28 | all right now we're going to going to |
| 07:29 | install the requirements and this is |
| 07:31 | where I started to run into some |
| 07:32 | problems so I may not run into it again |
| 07:34 | just because I've solved them already |
| 07:37 | but if I do I'll show it to you and even |
| 07:38 | if I don't I'll show you the problems I |
| 07:40 | had and I'll show you how I solved them |
| 07:42 | so we're going to type which python okay |
| 07:44 | and this is only because we want to make |
| 07:47 | sure that we're using the correct python |
| 07:49 | for installing with Pip so we grab the |
| 07:52 | python version we're using then we |
| 07:54 | simply paste that in type-m PIP install |
| 07:58 | dasr requirements. txt then hit enter so |
| 08:01 | one of the issues that I faced is that |
| 08:03 | this project requires rust and |
| 08:05 | specifically the dependency o Json |
| 08:09 | requires rust and I didn't have it |
| 08:11 | installed and so I had an error here so |
| 08:13 | I didn't have it this time so this is |
| 08:15 | going to be a little bit of behind the |
| 08:16 | scenes but anytime that I do a tutorial |
| 08:18 | video I go through it once without the |
| 08:20 | camera recording and I document every |
| 08:22 | step along the way and I also document |
| 08:25 | any errors or bugs that I run into so |
| 08:27 | that when I go to record I it doesn't |
| 08:29 | take me forever so I did have to install |
| 08:32 | rust and to do that I used this command |
| 08:36 | curl d-pro parentheses equals htps D- |
| 08:42 | tlsv1.2 |
| 08:44 | dssf and then so on and by the way I'll |
| 08:47 | drop all these commands in a GitHub gist |
| 08:49 | just so you have them and you don't have |
| 08:50 | to try to copy them and the next thing I |
| 08:53 | had to do was restart the terminal so |
| 08:54 | keep that in mind so one other thing I |
| 08:56 | want to point out another issue that I |
| 08:58 | ran into is the o Json issue and to |
| 09:01 | First fix it I installed rust and then I |
| 09:03 | ran into another issue with o Json and |
| 09:06 | to fix that I did this pip uninstall or |
| 09:09 | Json and then I installed it again using |
| 09:11 | this longer command which basically |
| 09:14 | installs the binary version that is |
| 09:16 | specific to my Apple silicon and that |
| 09:19 | was the problem and all of these |
| 09:21 | problems might be very specific to my |
| 09:22 | machine and you might run into other |
| 09:24 | problems I recommend Consulting Ai and |
| 09:27 | it will help you just copy paste |
| 09:28 | whatever issue you're running into and |
| 09:30 | it usually will give you some pretty |
| 09:31 | good suggestions so that command is PIP |
| 09:34 | install D- noach d-- only binary colon |
| 09:39 | all colon o Json and once I did that it |
| 09:42 | finally worked and if you do restart the |
| 09:45 | terminal you need to export the open AI |
| 09:47 | API key again because as soon as you |
| 09:49 | restart the terminal all of those |
| 09:51 | temporary environment variables are |
| 09:53 | wiped that's why using the EMV file is |
| 09:56 | always better all right now that that's |
| 09:58 | all done we're going to try try to spin |
| 09:59 | up the server and hopefully it works it |
| 10:01 | uses uicorn and this is the back end so |
| 10:04 | we need the back end and the front end |
| 10:05 | working so let me show you what to do |
| 10:07 | here uicorn open de. server. listen |
| 10:11 | Colona d-port 3000 now let's see if I |
| 10:14 | run into an issue last time when I tried |
| 10:16 | to spin up the server it would just |
| 10:18 | completely freeze and so I actually had |
| 10:20 | to restart the terminal anyway so we'll |
| 10:21 | see if we have to do that here all right |
| 10:23 | so it is looking like it's hanging again |
| 10:26 | unfortunately so what we're going to do |
| 10:28 | is hit controll C to try to quit out of |
| 10:30 | here although I think it's completely |
| 10:32 | Frozen so we're going to have to hit |
| 10:33 | contrl Z and that'll force quit it and |
| 10:36 | so let's try it again and if this |
| 10:39 | doesn't work I'm going to try restarting |
| 10:40 | the terminal completely again all right |
| 10:43 | maybe I'm being a bit impatient but I |
| 10:45 | don't think it's working so I'm going to |
| 10:46 | hit oh I spoke too soon look at that so |
| 10:49 | the second time it did work maybe it's |
| 10:51 | doing some downloads in the background |
| 10:52 | I'm not sure but it did work on the |
| 10:54 | second go so we have uicorn running at |
| 10:57 | Local Host 3000 perfect |
| 10:59 | now what we're going to do is we need to |
| 11:01 | now install and spin up the front end so |
| 11:04 | we click the little plus button right |
| 11:06 | here we wait till we get our new |
| 11:08 | terminal up and running we're still in |
| 11:10 | the open Devon folder and we still have |
| 11:12 | OD cond environment running so just |
| 11:14 | verify those things now we're going to |
| 11:17 | CD into the folder called front end and |
| 11:21 | we're going to be using node to install |
| 11:23 | it an npm and if you don't have node if |
| 11:25 | you don't have npm you need to go Google |
| 11:27 | that and or use Claud or GP or something |
| 11:30 | and just get those two things installed |
| 11:32 | it should be pretty straightforward I |
| 11:34 | believe if you're using a Mac you can |
| 11:35 | even use Brew so you could do like Brew |
| 11:37 | install npm and it should work I believe |
| 11:41 | all right so there it is so that would |
| 11:43 | work so now we have npm installed all |
| 11:45 | right so now that we have node installed |
| 11:48 | let's do npm install and that's going to |
| 11:51 | install all the front-end packages now |
| 11:53 | luckily I have much fewer issues using |
| 11:57 | npm and the whole node e ecosystem and |
| 12:00 | package management with node much fewer |
| 12:02 | issues than I do with python so |
| 12:04 | hopefully you don't run into anything |
| 12:05 | okay now that we have all of the node |
| 12:08 | packages installed we are simply going |
| 12:10 | to spin up the node server now so npm |
| 12:13 | run start-- space- dport space 3001 and |
| 12:17 | then hit enter and that's it we should |
| 12:19 | be up and running now let's give it a |
| 12:21 | try so I'm going to click on this Local |
| 12:23 | Host right there actually I'm going to |
| 12:25 | hold down command then click on the |
| 12:26 | local host and there we go open Dev |
| 12:29 | it worked wonderful so it takes a few |
| 12:32 | seconds to initialize the agent and I'm |
| 12:34 | going to switch to GPT 4 over here and |
| 12:36 | there we go hello I'm open Devon what |
| 12:38 | would you like me to build so I'll say a |
| 12:40 | simple website that says hello world and |
| 12:42 | now we'll see it working a little bit |
| 12:44 | starting new task we can also click over |
| 12:46 | to the planner now I've noticed the |
| 12:48 | planner doesn't really update that often |
| 12:50 | or maybe even at all um maybe that's a |
| 12:53 | little buggy I've also found the browser |
| 12:55 | doesn't really work all that well to be |
| 12:57 | honest the terminal seems to work great |
| 12:59 | and the code editor definitely works so |
| 13:02 | I mean there is the code there's the |
| 13:03 | hello world HTML file perfectly done so |
| 13:06 | here we go it's starting up a server all |
| 13:08 | by itself and it visited Local Host 8000 |
| 13:13 | so if I actually go over to the browser |
| 13:14 | it did switch and go over to Local Host |
| 13:16 | 8000 so it kind of works but there's |
| 13:19 | some little bug and it doesn't work |
| 13:21 | completely yeah and if I go back to the |
| 13:23 | logs from the back end I can see that |
| 13:26 | there was an error here and it exited so |
| 13:28 | that's it it so definitely still buggy |
| 13:31 | but they're making a ton of great |
| 13:32 | progress now let me show you how to use |
| 13:35 | basically any model including a locally |
| 13:37 | run open source model so if you wanted |
| 13:39 | to use Claud you just export these |
| 13:42 | things right here so the llm API key and |
| 13:44 | then the llm model you export this and |
| 13:47 | you do that from terminal now if you did |
| 13:50 | want to use a local model you do llm |
| 13:52 | base URL and you change it to Local Host |
| 13:55 | 3000 and then you can use LM Studio you |
| 13:58 | can use ol llama you can use anything |
| 14:00 | you want as long as it exposes an open |
| 14:02 | AI compatible API endpoint and you can |
| 14:06 | even select llama 2 for your embedding |
| 14:08 | model which is really cool so you could |
| 14:11 | technically get this to be completely |
| 14:13 | local if you wanted so they are truly |
| 14:16 | trying to mimic what Devon has done and |
| 14:19 | Devon is super impressive it is |
| 14:21 | definitely not the first time we've had |
| 14:23 | coding assistance it's actually far from |
| 14:25 | it but it is one of the most if not the |
| 14:27 | most polished user interface that I've |
| 14:29 | seen so I'm really excited for open |
| 14:32 | Devon I've tried this other project DEA |
| 14:34 | a bunch and I haven't gotten it to work |
| 14:36 | but open Devon works pretty darn well so |
| 14:38 | give it a try create issues on their |
| 14:41 | GitHub repository as you come across |
| 14:42 | them contribute if you're open to that |
| 14:45 | and open Devon can be something really |
| 14:47 | special that helps developers and even |
| 14:49 | non-developers be really productive at |
| 14:52 | building code if you liked this video |
| 14:54 | please consider giving a like And |
| 14:55 | subscribe and I'll see you in the next |
| 14:57 | one |
