# Transcript: Cursor Composer: MULTI-FILE AI Coding for engineers that SHIP

[Watch Video](https://www.youtube.com/watch?v=V9_RzjqCXP8&t=662s)

| Timestamp | Text |
|-----------|------|
| 00:00 | AI coding is changing the way software |
| 00:03 | is created and there's one team and one |
| 00:06 | lone 20x engineer leading the way for |
| 00:10 | you and I cursor is the team the cursor |
| 00:14 | team has made significant strides in AI |
| 00:17 | coding but there's one feature they've |
| 00:19 | developed that stands far Above the Rest |
| 00:23 | everything else pills in comparison in |
| 00:25 | this video I'll show you what this |
| 00:27 | feature is and why it's so important |
| 00:30 | this feature is so new it doesn't have |
| 00:31 | any real true documentation yet but if |
| 00:34 | you visit the change log you can see |
| 00:36 | exactly what this feature is this is |
| 00:38 | none other than cursor's brand new |
| 00:41 | composer feature the main trick here is |
| 00:44 | that it is the new experimental multi |
| 00:47 | file editing feature let's dive into |
| 00:55 | it so in order to enable cursor composer |
| 00:58 | feature you can go into to your settings |
| 01:00 | go to the beta Flags make sure that |
| 01:02 | composer is enabled here once you've |
| 01:04 | done that command I will pop up a small |
| 01:06 | composer window and command shift I will |
| 01:09 | pop up a full screen version let's go |
| 01:12 | ahead and write a change and let's |
| 01:14 | convert this input and this output |
| 01:16 | variable here you can see in this |
| 01:17 | component let's go ahead and give this a |
| 01:21 | true input field and a true output field |
| 01:23 | let's open up cursor composer let's go |
| 01:26 | ahead and try out the brand new chat GPT |
| 01:28 | 4 latest model I'll prompt convert input |
| 01:33 | into a real input field make the input |
| 01:37 | dark blue and white text we'll hit enter |
| 01:41 | and you can see it's focusing one file |
| 01:44 | at a time right now we only have liquid |
| 01:46 | prompt. viw in our context and there you |
| 01:50 | can see the changes getting written I'll |
| 01:53 | go ahead accept these changes you can |
| 01:55 | see here we have input ping how are you |
| 01:58 | it updated this to an input field and |
| 02:00 | now we have a label let's go ahead and |
| 02:02 | make a similar update to our output |
| 02:04 | field with the difference being we want |
| 02:07 | to take this output field and convert it |
| 02:08 | into a markdown component that we're |
| 02:11 | using in another component somewhere |
| 02:13 | else so what I'll do is I'll H command |
| 02:15 | in to start a new chat add another file |
| 02:18 | to the context so the change I'm looking |
| 02:21 | for is also in this prompt editor all |
| 02:24 | I'll do is reference it and then I'll |
| 02:26 | say convert output to a DC component and |
| 02:31 | render The Prompt output |
| 02:40 | there cool so it picked up on this |
| 02:43 | component here I'll go ahead and hit |
| 02:44 | accept all so we can take a look at |
| 02:45 | these changes and now we're rendering |
| 02:48 | this in this MDC component this is great |
| 02:51 | let's go ahead and test out some of the |
| 02:52 | multifile editing features that this |
| 02:54 | gives us right because that's the whole |
| 02:56 | point we can already do this using |
| 02:58 | cursor you know we could have made all |
| 02:59 | those changes using the endline |
| 03:01 | selection prompt the benefit and the |
| 03:03 | value of this brand new composer editor |
| 03:06 | is that we can write a multiple |
| 03:10 | files so what I'll say here is move the |
| 03:14 | input |
| 03:16 | field into its own liquid input and I'll |
| 03:21 | specify the directory as |
| 03:23 | well component same with the output |
| 03:29 | field |
| 03:30 | you can see here we're actually going to |
| 03:32 | generate that component we have the |
| 03:33 | liquid input liquid output and these |
| 03:36 | files have now been created and now |
| 03:39 | they're getting referenced right so go |
| 03:40 | ahead accept all now we have this error |
| 03:42 | here I'm not going to do anything |
| 03:44 | manually I'm just going to highlight |
| 03:45 | this I'm going to come back over to |
| 03:47 | composer I'm going to paste this in |
| 03:49 | resolve this error and then I'll go |
| 03:52 | ahead and just add those new files right |
| 03:53 | so I'll add input I'll add output and |
| 03:56 | let it rip so I'm still testing out the |
| 03:58 | capabilities of chat GP 40 from what I |
| 04:00 | can tell it seems like a very capable |
| 04:02 | model but it's not as consistent and |
| 04:05 | it's not as solid as a model like Sonic |
| 04:07 | 3.5 so it's going to break this model |
| 04:10 | into both a value and an input that |
| 04:13 | looks great I'll accept that and let's |
| 04:15 | go ahead and refresh and that looks |
| 04:17 | great looks like we have our rendering |
| 04:19 | back up and writing there so there's an |
| 04:21 | example of using cursor composer feature |
| 04:23 | to write multiple components at the |
| 04:25 | exact same time right so this is pretty |
| 04:27 | cool to see let's go ahead and push this |
| 04:29 | further I want to go ahead and improve |
| 04:31 | the styling of both these components so |
| 04:33 | I'm going to use cursor composers |
| 04:35 | overlay feature for this so I'm going to |
| 04:37 | use command shift I here so you can see |
| 04:39 | we have this new composer button I'm |
| 04:41 | going to go ahead and click that and |
| 04:42 | start adding the context needed to make |
| 04:44 | these changes so I'm going to go ahead |
| 04:46 | I'm going to add the liquid prompt input |
| 04:49 | and output and now we have those files |
| 04:52 | in our context so now I can go ahead and |
| 04:54 | just prompt whatever I'm looking for to |
| 04:56 | make the changes and we can keep testing |
| 04:58 | J GPT for o latest on top of composer |
| 05:02 | I'm going to go ahead and add one more |
| 05:03 | file here there's a reference file that |
| 05:05 | I used before um that I want to go ahead |
| 05:07 | and just kind of get some of the styles |
| 05:08 | from so I'm going to go ahead and add |
| 05:10 | prompt editor as well this is an |
| 05:12 | existing code base uh let me just go |
| 05:14 | ahead and show you the size here if I |
| 05:17 | come in here and look for for regx um I |
| 05:21 | had this before so yeah if we look at |
| 05:23 | total so this code base has about 22,000 |
| 05:25 | lines of code and if we do what was it |
| 05:29 | grab Dash C we can see that we have |
| 05:31 | about 151 files specifically TTS and |
| 05:35 | view file so you know this is a |
| 05:37 | fullstack code base it's a n application |
| 05:39 | this is in production this is Live code |
| 05:41 | with multifile editing with these AI |
| 05:43 | coding tools we're operating on about |
| 05:45 | 151 across typescript and VJs and then |
| 05:48 | about 22,000 lines of code so this is a |
| 05:51 | small production code base there are |
| 05:53 | code bases I'm sure you've seen and |
| 05:54 | worked with that are much larger |
| 05:56 | especially if you're mid or senior level |
| 05:57 | 150 files this is fairly sizable and uh |
| 06:01 | you know of course it'll continue to |
| 06:02 | grow in size as the product grows but |
| 06:04 | let's go ahead and hop back to our uh |
| 06:06 | composer menu here looks like we lost |
| 06:08 | the file references so I'm just going to |
| 06:10 | add those back here we had the input |
| 06:11 | output and the prompt editor and um what |
| 06:14 | we're going to do here is say style |
| 06:18 | the uh liquid input and liquid output to |
| 06:23 | mirror The Prompt |
| 06:26 | editor I'll just go ahead and leave that |
| 06:28 | as it is right so we're asking the |
| 06:30 | assistant to look at these four files |
| 06:33 | pull these styles from the prompt editor |
| 06:35 | and apply them to our liquid input and |
| 06:38 | our liquid output so this is really cool |
| 06:40 | you can see let me just go ahead and |
| 06:42 | open this up a little bit so this is |
| 06:44 | really cool right so on the right panel |
| 06:46 | here you can see it walking through the |
| 06:48 | changes giving an explanation and once |
| 06:50 | we click the file it's going to show off |
| 06:53 | the changes needed for each respective |
| 06:55 | file right so this is really cool to see |
| 06:57 | it's really breaking it down and showing |
| 06:59 | exact changes it's making across |
| 07:00 | multiple files I'll go ahead here I'll |
| 07:03 | hit accept all and you can see here we |
| 07:05 | have some styling so not the best |
| 07:07 | styling it looks like you know it's not |
| 07:09 | exactly what we were looking for but |
| 07:11 | it's close enough uh remove the |
| 07:13 | background from the input |
| 07:17 | section and delete input colon delete |
| 07:20 | the label right so just making a couple |
| 07:22 | more tweaks here it's not exactly the |
| 07:24 | way I want it so I'm just going to keep |
| 07:26 | tweaking to get the results I'm looking |
| 07:28 | for so you can see there and that |
| 07:29 | iteration it only updated liquid input |
| 07:31 | I'll just hit accept all and you can see |
| 07:33 | in the UI it dropped that and it looks |
| 07:35 | like it did drop the background on the |
| 07:37 | button as well put the background back |
| 07:40 | on the input HTML |
| 07:45 | element okay so again I'll accept and |
| 07:47 | there we go so we got the background |
| 07:49 | back that looks good um now I want to |
| 07:50 | Center these items it's kind of like |
| 07:52 | clunky right there so and if you want to |
| 07:54 | close this you just hit Escape so now |
| 07:56 | you you know you're back in your regular |
| 07:57 | IDE editing mode which is fantastic we |
| 08:00 | can go over to the liquid prompt and now |
| 08:02 | I want to give this uh something to |
| 08:04 | reference by right prompt editor and |
| 08:07 | then I'll just say I'll start a new chat |
| 08:09 | here just because we don't need all the |
| 08:11 | context I'll just go to the liquid |
| 08:12 | prompt and I'll say Center the |
| 08:15 | vertically and horizontally right so |
| 08:18 | just go ahead prompt that let it get to |
| 08:21 | work there and looks like that's good |
| 08:24 | I'll go ahead and hit accept and now you |
| 08:26 | can see that there it's going left to |
| 08:28 | right so of course the fix for this is |
| 08:31 | uh Flex call so just literally say Flex |
| 08:33 | call let it make that change with the |
| 08:36 | context of the previous conversation hit |
| 08:38 | accept and now we have this right so you |
| 08:40 | know this is just like classic styling |
| 08:42 | classic CSS writing um make the width of |
| 08:47 | the uh liquid input the same match the |
| 08:51 | input |
| 08:52 | field I'm just doing this as a test I |
| 08:54 | actually don't know if this will work |
| 08:55 | what I'm hoping will happen here is that |
| 08:56 | it automatically adds the files uh the |
| 08:59 | content inside liquid input and output |
| 09:02 | to the context and makes this change so |
| 09:04 | let's go ahead and just see if it it |
| 09:05 | does that this is actually a test I'm |
| 09:07 | not sure if this will work let's go |
| 09:08 | ahead and try okay yeah so that's not |
| 09:09 | working right it is only looking at the |
| 09:11 | files that it has in its context and it |
| 09:14 | just does that to the top level so |
| 09:15 | that's fine what I'll do here is I'll |
| 09:17 | hit uh reject all and then I'll add |
| 09:20 | these files to the context right so this |
| 09:22 | is really cool after execution I can |
| 09:24 | just go ahead and add these and then |
| 09:26 | I'll look for my previous message here |
| 09:28 | I'll just throw this in here right so |
| 09:30 | now I'm going to paste this message in |
| 09:31 | again and see how it does with the |
| 09:32 | context of the files so you can see now |
| 09:35 | we're editing the input and the output |
| 09:38 | and we also are editing the liquid |
| 09:40 | prompt which I'm not sure if we need to |
| 09:43 | do that let's go ahead and take a look |
| 09:44 | here um input output width and we're |
| 09:47 | setting that to Max with 500 pixels okay |
| 09:49 | so that looks fine I'll go ahead and |
| 09:50 | just accept this and now we should get |
| 09:52 | some matching width roughly okay so |
| 09:56 | whatever that looks fine um I'll just do |
| 09:58 | one more I'll say Gap or okay Gap nine I |
| 10:01 | guess I'm just doing some adding a gap |
| 10:04 | here to these items and we'll just |
| 10:07 | accept and there we go right so great so |
| 10:09 | now we have |
| 10:09 | [Music] |
| 10:12 | that okay so that's good uh we're making |
| 10:14 | a couple changes right this is just |
| 10:15 | small you know frontend stuff but it's |
| 10:18 | really nice because what we're doing |
| 10:19 | here is we're kind of moving oursel up |
| 10:21 | the stack we're not writing the stuff |
| 10:23 | manually by hand anymore we're asking |
| 10:25 | for what we want done at a higher level |
| 10:27 | and then we're letting the llm we're |
| 10:28 | letting our models our AI powered IDE |
| 10:31 | cursor uh we're letting this stuff do |
| 10:33 | the hard work for us right now we need |
| 10:35 | to when we press the enter key I want |
| 10:37 | whatever prompt is in here to actually |
| 10:39 | execute we're going to keep these files |
| 10:40 | context here on Enter key when liquid |
| 10:46 | prompt run a new prompt up to liquid |
| 10:50 | prompt of and run the make prompt |
| 10:54 | function so long story short here is in |
| 10:57 | the liquid prompt file we have this make |
| 11:00 | prompt function here that is coming out |
| 11:02 | of a hook and all this does is you know |
| 11:04 | it runs prompt and it Returns the result |
| 11:07 | right it sets it to the prompt output |
| 11:10 | right here we want when we press the |
| 11:11 | enter key on the input field instead of |
| 11:13 | doing this in our mounted hook we want |
| 11:16 | you know these components to just handle |
| 11:18 | that for us so what we'll do is open |
| 11:20 | this up again and we'll just let that |
| 11:22 | fire so let's see how gpg 40 and |
| 11:25 | composer does this for us here okay so |
| 11:27 | it knows to update the input field here |
| 11:30 | this is awesome it has that Enter key |
| 11:31 | event set up and now it's writing |
| 11:36 | that uh higher level method on the |
| 11:39 | liquid prompt so uh this all looks good |
| 11:42 | so I'll just hit accept all I'll say |
| 11:44 | remove handle enter from unmounted so |
| 11:48 | I'm just saying you know don't fire that |
| 11:49 | event off on the unmounted hook we'll |
| 11:52 | just do that from our mitted event so |
| 11:55 | okay that looks good I'll accept close |
| 11:58 | this and now we see this looking good um |
| 12:02 | ping how are you I'll hit |
| 12:04 | enter there it is so now it is you know |
| 12:07 | giving us that content I don't know what |
| 12:09 | model we're using right here so I'm just |
| 12:11 | going to go ahead and just you know |
| 12:12 | right a quick prompt to create an input |
| 12:14 | field for that so I'll say I'll do this |
| 12:16 | in a small quick composer window here so |
| 12:19 | I'll just come in here um I'll hit |
| 12:22 | command new and I'll just say move the |
| 12:25 | model into a ref show it |
| 12:29 | above the liquid input |
| 12:37 | field cool so I'll accept that and close |
| 12:42 | this let's go ahead and see what the |
| 12:44 | model is good so we have gb4 mini |
| 12:46 | running here and it's just going to show |
| 12:48 | that right at the top that's fine um |
| 12:51 | let's go and just take a look at what |
| 12:52 | that looks like again okay that's |
| 12:54 | whatever looks good and now if I hit |
| 12:57 | enter here we're going to get the result |
| 12:59 | results out there and type another |
| 13:00 | prompt I'll say count to five okay 1 2 3 |
| 13:04 | 4 5 very cool count to |
| 13:08 | 10 and I'll say in reverse and I'll say |
| 13:12 | skip evens so you can tell this is a |
| 13:14 | real llm Runing under the hood right |
| 13:16 | skip three good skip |
| 13:20 | n nice okay so you can tell right this |
| 13:23 | is a model running under the hood that's |
| 13:24 | great so let's go ahe and do a couple |
| 13:26 | more things here I don't like this blue |
| 13:28 | color and they the idea behind the |
| 13:30 | liquid prompt editor here is that I want |
| 13:31 | to show and hide this prompt editor no |
| 13:34 | matter where I am we'll of course use |
| 13:36 | composer for this so I'm going to switch |
| 13:38 | to the liquid input file and start a new |
| 13:42 | message here and the nice part about |
| 13:44 | this is whatever file you have Focus |
| 13:46 | it's going to automatically start the |
| 13:48 | context with just that file there's the |
| 13:51 | background color obviously we can tweak |
| 13:52 | that update the background |
| 13:55 | color and dark blue left to red right or |
| 13:59 | no no no I'll say uh two top right so |
| 14:04 | we'll see these changes come in here |
| 14:06 | perfect and there's that gradient and |
| 14:09 | okay so uh we'll allow that for now and |
| 14:12 | then I want to come back in here uh just |
| 14:14 | making some small tweaks just kind of |
| 14:16 | moving fast doing whatever convert the |
| 14:19 | model dip to a p and it should come in |
| 14:22 | and just highlight this one line here |
| 14:24 | great I'll accept that cool nice so now |
| 14:28 | it has our font there that's awesome and |
| 14:31 | now we'll we'll ask for our keyboard |
| 14:34 | event so what I'll say here is using VI |
| 14:36 | use slash on keystroke I think it is |
| 14:40 | show and hide the liquid prompt editor |
| 14:45 | div and I'll say add a ref for the show |
| 14:51 | hide uh VAR okay so I'll just let that |
| 14:54 | rip this is just a single file edit |
| 14:56 | let's go ahead and see if it can do this |
| 14:58 | I did forget to mention the exact key |
| 15:01 | binding that I wanted so we'll add that |
| 15:03 | up in a follow-up prompt you can see |
| 15:05 | here we did get this uh solid import we |
| 15:08 | got the variable we wanted and we have |
| 15:12 | the keystroke which is good so that's |
| 15:14 | pretty close so go ahead and accept this |
| 15:16 | and then I'll go ahead and what do we |
| 15:19 | get here let's go a and refresh oh so we |
| 15:21 | have this bug here right so we have a |
| 15:22 | full-on error so I'll say fix error bad |
| 15:26 | comment line n okay good just going to |
| 15:29 | go ahead and fix that for us awesome |
| 15:30 | looks good default show prompt |
| 15:33 | editor def false on key |
| 15:36 | stroke command plus P to show and hide |
| 15:41 | that VAR keep Escape as well so it |
| 15:45 | shouldn't need to touch any of the other |
| 15:47 | files that we have here okay nice that |
| 15:50 | looks good I think this can accept a |
| 15:52 | list we'll see so I'll go ahead and |
| 15:54 | accept that and now it's show default |
| 15:57 | false I'll hit command p and of course |
| 15:59 | we're getting the classic print so I'll |
| 16:01 | say I believe the Onkey stroke uh yeah |
| 16:04 | put places the event here right so event |
| 16:06 | and then we have the keyboard event and |
| 16:08 | then we have to you know do that |
| 16:10 | manually so I'll just use cursor tab |
| 16:12 | here to do these Auto completions |
| 16:13 | another incredible feature from the |
| 16:15 | cursor team but so let's go ahead and |
| 16:17 | try this now |
| 16:19 | right all right so it looks like these |
| 16:21 | key combinations aren't working with on |
| 16:23 | keystroke they're just not supported |
| 16:24 | like this it only handles the individual |
| 16:27 | button presses that's fine what'll I'll |
| 16:29 | do here is I'll come in and I'll just |
| 16:30 | add show and hide this right it's |
| 16:32 | actually faster so that's good now we're |
| 16:34 | showing and hiding that now we have this |
| 16:36 | small super simple prompt editor that we |
| 16:38 | can you know ideally we can you know |
| 16:40 | convert portion into its own component |
| 16:42 | and then just kind of place wherever we |
| 16:44 | want to right so let's move this content |
| 16:47 | and the relevant scripting into its own |
| 16:50 | component so just like we did for liquid |
| 16:52 | input and output let's go ahead and just |
| 16:54 | move you know all this content here into |
| 16:56 | its own component um I'm going to use |
| 16:59 | the larger editor for this and start a |
| 17:01 | new |
| 17:02 | composer and all I'll do is load the |
| 17:05 | liquid prompt move the and what do we |
| 17:08 | call this liquid prompt |
| 17:11 | editor uhu move the liquid prompt editor |
| 17:14 | and all related State into its own |
| 17:18 | component and we'll say call it liquid |
| 17:21 | prompt editor. view okay so now we're |
| 17:24 | going to ask for all of it to be moved |
| 17:26 | into its own component |
| 17:29 | it's going to do all the importing it |
| 17:31 | needs and then it's going to also update |
| 17:33 | the top level uh liquid prompt just as |
| 17:37 | before it looks like it is going to miss |
| 17:40 | the on keystroke event so I'll say don't |
| 17:43 | forget to move the on |
| 17:46 | keystroke into the |
| 17:49 | component and I'll send that as a |
| 17:55 | followup perfect and then all we're left |
| 17:58 | with here in the previous component is |
| 18:00 | just the top level items that we had |
| 18:01 | before a couple unused variables couple |
| 18:04 | hooks whatever so I'll go ahead accept |
| 18:06 | all changes you can see we have the |
| 18:08 | first change here this is the brand new |
| 18:10 | liquid prompt editor file it created |
| 18:12 | this entire file for us and then we have |
| 18:14 | the previous liquid prompt. viw file |
| 18:16 | which just has you know a couple |
| 18:18 | additional uh components and the editor |
| 18:20 | itself so I'll accept Okay so looks like |
| 18:22 | we have an error that's totally fine |
| 18:24 | again I'm just going to copy all this we |
| 18:26 | have an unknown keywords open up compos |
| 18:29 | again going to start a new window I'm |
| 18:30 | going to add our new file here and I'll |
| 18:32 | say resolve this |
| 18:36 | issue okay so just got this |
| 18:39 | unnecessary variable here I'll I'll just |
| 18:41 | say just remove unsub okay so that looks |
| 18:44 | good let's make sure liquid prompt |
| 18:47 | changes are also looking good uh we |
| 18:49 | don't need this composable here at all |
| 18:52 | drop the use prompt editor |
| 18:56 | import next part about no this is |
| 18:58 | automatically imported for us so just |
| 19:00 | going to ask it to drop that for us uh |
| 19:02 | no need for that okay now it's trying to |
| 19:05 | delete other code so it thinks I wanted |
| 19:07 | to remove all of it it's kind of being |
| 19:08 | too smart in a way so this could be |
| 19:11 | easily solved with a system prompt where |
| 19:13 | I say hey we're using n um in N we |
| 19:16 | automatically have all of our Hooks and |
| 19:18 | our components imported we also don't |
| 19:21 | need any view Imports you can do that |
| 19:23 | through the system prompt message in the |
| 19:25 | cursor settings I'm just going to ask it |
| 19:27 | to undo these changes so undo |
| 19:29 | uh just don't |
| 19:31 | import keep the handle enter |
| 19:35 | functionality the |
| 19:43 | same okay so this is fine I'm going to |
| 19:45 | hit accept all and then I'm just going |
| 19:46 | to drop this change back in so that it |
| 19:49 | has that and let's go ahead and make |
| 19:52 | sure it all still works great so this is |
| 19:54 | pretty cool right |
| 19:59 | so a couple bumps a couple hiccups I |
| 20:01 | personally am still trying to figure out |
| 20:03 | exactly uh where the capabilities of |
| 20:06 | composer are but also you know every |
| 20:09 | model that you use here operates |
| 20:11 | differently if you're using AER or |
| 20:13 | continue or any other type of AI coding |
| 20:16 | tool you really have to see and kind of |
| 20:18 | play with how the model performs every |
| 20:20 | model performs different with every |
| 20:22 | different tool remember that the |
| 20:24 | engineers the people building out these |
| 20:26 | tools they are writing prompts and |
| 20:28 | prompt has a different impact and every |
| 20:30 | prompt has a different impact with |
| 20:32 | different models chbt 40 is super new |
| 20:35 | super bleeding edge I'm going to say you |
| 20:37 | know keep using claw 3.5 Sonic for |
| 20:39 | coding with some of these models you |
| 20:41 | can't really just look at the benchmarks |
| 20:42 | and know how it will perform um I can |
| 20:44 | tell you and I've been saying this for a |
| 20:46 | while and if you're actually writing |
| 20:47 | code with AI you know this as well claw |
| 20:49 | 3.5 Sonet is the king of AI coding and |
| 20:52 | it integrates the best with coding tools |
| 20:55 | just trying out gpg 40 here I can tell |
| 20:57 | you that uh Sonet wouldn't have made |
| 20:59 | some of the mistakes that CBT 40 made |
| 21:02 | and that has nothing to do with the |
| 21:04 | composer feature from the cursor team so |
| 21:06 | this is really cool right with this |
| 21:08 | brand new composer feature we now have |
| 21:10 | multifile editing inside of the cursor |
| 21:12 | IDE with it we were able to fairly |
| 21:15 | quickly build out a simple prompt |
| 21:17 | editing tool if you want the insane |
| 21:19 | productivity gains that are available to |
| 21:22 | you you need to be using the incredible |
| 21:23 | AI coding tools that unlock these |
| 21:25 | capabilities for you right so we're |
| 21:27 | talking about cursor and we're talking |
| 21:28 | about AER these are the two AI coding |
| 21:30 | tools leading the way writing code is |
| 21:33 | cheaper and faster than ever I am just |
| 21:37 | getting started using this composer |
| 21:38 | feature I I discovered it this past week |
| 21:40 | and I've been really digging in honestly |
| 21:42 | before this feature I was moving more |
| 21:44 | and more away from cursor uh multifile |
| 21:46 | editing is a massive killer feature for |
| 21:48 | AI coding it allows you to write code |
| 21:51 | like you actually do which is across you |
| 21:53 | know 5 10 sometimes 20 files at the same |
| 21:56 | time so this is really powerful |
| 21:57 | especially for the you know mid senior |
| 21:59 | level Engineers that are making changes |
| 22:01 | across large code bases this is a |
| 22:03 | smaller code base only you know 150 |
| 22:06 | files but this is a tool that you can |
| 22:07 | use on real production code bases |
| 22:09 | cursor's new composer feature really |
| 22:11 | allows you to unlock multifile editing |
| 22:14 | which is like I mentioned a massive |
| 22:16 | massive must for writing code on |
| 22:19 | production code bases as large lingers |
| 22:22 | models improve and we get Claude 3.5 |
| 22:25 | Opus we get GPT NEX we get strawberry we |
| 22:28 | get Gemini 1.5 Ultra you'll be able to |
| 22:31 | lean more and more into these multifile |
| 22:33 | editing capabilities big shout out to |
| 22:35 | the cursor team you guys are doing great |
| 22:37 | work um and you know at the beginning I |
| 22:39 | mentioned the lone 20x engineer that is |
| 22:42 | none other than Paul working on AER I |
| 22:45 | recommend both these tools for AI coding |
| 22:48 | since the beginning these two tools have |
| 22:50 | been my favorite uh Paul is building AER |
| 22:52 | and the cursor team is building cursor |
| 22:54 | of course these are my recommendations |
| 22:56 | for AI coding as many AI coding tools as |
| 22:58 | I've tried I keep coming back to these |
| 23:01 | two and I keep sharing these two on the |
| 23:03 | channel for a good reason they're the |
| 23:05 | best two tools you can use to multiply |
| 23:08 | your output as an engineer these tools |
| 23:10 | are also really important and Powerful |
| 23:12 | because they're focusing on the |
| 23:14 | experience of the engineer they're |
| 23:16 | focusing on what it's actually like to |
| 23:18 | be in a code base with hundreds and |
| 23:20 | hundreds and thousands of files with |
| 23:22 | hundreds of thousands of lines of code |
| 23:24 | both AER and cursor are the products |
| 23:26 | that understand that and they're |
| 23:27 | building out the experience for us |
| 23:29 | Engineers big shout out to both of them |
| 23:31 | I'm going to be covering both these |
| 23:32 | tools more on the channel as I have for |
| 23:35 | the past year or so I'll link a couple |
| 23:37 | of the previous videos if you're super |
| 23:38 | amped on AI coding those will be in the |
| 23:40 | description for you you can check those |
| 23:42 | out I hope this demo of cursor's new |
| 23:44 | composer feature was helpful for you if |
| 23:47 | it was you know what to do drop the like |
| 23:48 | drop the sub leave a comment let me know |
| 23:50 | how your AI coding is going let me know |
| 23:53 | how much you're using these tools big |
| 23:54 | thanks and I'll see you in the next one |
| 23:58 | for |
