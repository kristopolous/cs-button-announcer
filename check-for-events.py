#!/usr/bin/env python3
from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timezone, timedelta
import pytz
import random

service = build('calendar', 'v3', 
                credentials = service_account.Credentials.from_service_account_file('secrets.json', scopes=['https://www.googleapis.com/auth/calendar.readonly']))

now = datetime.now(pytz.timezone('America/Los_Angeles'))

events_result = service.events().list(
    calendarId='crashspacela@gmail.com',
    timeMin=(now - timedelta(minutes=20)).isoformat(),
    timeMax=(now + timedelta(minutes=20)).isoformat(),
    singleEvents=True
).execute()

events = events_result.get('items', [])
if events:
    print(f'<h1>{events[0]["summary"]}</h1>\n<p>{events[0]["description"]}</p><hr>')
else:
    title = random.choice([
        "Secret Time",
        "Under Wraps",
        "Off the Books",
        "Low Profile",
        "Covert Ops",
        "Quiet Time",
        "Stealth Mode",
        "Surprise Session",
        "Hidden Hours",
        "Unplanned Spark",
        "Idle Hands",
        "Free Play",
        "Surprise Slot",
        "Hidden Workshop",
        "Open Streak",
        "Silent Hours",
        "Incognito Mode"])
    descr = random.choice([
        "Oh, Crash Space! Your tools work all day long, From dawn till dusk, we labor with song. The <strong>CNC</strong> hums, the <strong>laser cutter</strong> glows bright, In your hallowed halls, we build through the night.",
        "March on, O makers, with hammer and saw, In <strong>Crash Space</strong>, we craft without flaw. The <strong>Prusa</strong> spins, and the woodplanes do fly, Together we rise, and together we try!",
        "Oh, mighty <strong>woodshop</strong> and the <strong>electronics</strong> bench, Your tools are sharp, your craft never a wrench. With every cut, and every spark, We shape the future, we leave our mark!",
        "Hail, <strong>Crash Space</strong>, where the dreamers unite, With your machines, we create what’s right. Through the sweat and the toil, our spirits don’t fade, In your workshop of wonders, all visions are made!",
        "March, march onward, in <strong>Crash Space</strong> we trust, With <em>Chill Bill</em> keeping the air cool and just. The <strong>3D printers</strong> hum, and the saws will sing, For in <strong>Crash Space</strong>, our dreams take wing!"
        "Entering <strong>Crash Space</strong> felt like stepping into a creative playground. Every room held something new—whether it was the buzz of the <strong>laser cutter</strong> or the quiet hum of the <strong>woodshop</strong>. <em>Chill Bill</em> kept everything cool, setting the perfect stage for the next big idea.",
        "The doors to <strong>Crash Space</strong> opened, and instantly the room felt alive with possibility. The <strong>electronics equipment</strong> hummed in the corner, while the <strong>woodshop</strong> invited me to create something new. Everything about the space was ready to turn ideas into reality.",
        "As soon as I stepped into <strong>Crash Space</strong>, I could feel the energy of the place. The <strong>CNC machine</strong> stood ready, the <strong>woodshop</strong> smelled like freshly cut timber, and <strong>Chill Bill</strong> made sure the air was just right to get started.",
        "Walking into <strong>Crash Space</strong> was like stepping into the future of creativity. The <strong>laser cutter</strong> sat in the corner, waiting for inspiration, while the <strong>Prusa 3D printers</strong> stood by for whatever new project I had in mind. With <em>Chill Bill</em> keeping things cool, the space was set for a productive session.",
        "Entering <strong>Crash Space</strong> felt like discovering a hidden treasure trove of tools and ideas. The <strong>electronics equipment</strong> was ready for action, and the <strong>woodshop</strong> promised new creations. <em>Chill Bill</em> made sure the atmosphere was perfect for getting creative.",
        "The moment I stepped inside <strong>Crash Space</strong>, the energy shifted. The <strong>laser cutter</strong> hummed softly, the <strong>woodshop</strong> was alive with possibility, and the <strong>CNC machine</strong> stood ready for whatever project I had in mind. It was time to make something great.",
        "There’s something about <strong>Crash Space</strong> that feels different every time you enter. The <strong>electronics equipment</strong> flickered to life, while the <strong>woodshop</strong> whispered its secrets. With <em>Chill Bill</em> ensuring the perfect temperature, I was ready to dive into something new.",
        "In <strong>Crash Space</strong>, every room invites you to create. Whether you're drawn to the <strong>Prusa 3D printers</strong> or the <strong>laser cutter</strong>, the space is designed for making things happen. <em>Chill Bill</em> kept everything cool, so I could get to work on whatever was next.",
        "The moment I entered <strong>Crash Space</strong>, I was greeted with the soft hum of creation. The <strong>CNC machine</strong> awaited my next project, the <strong>electronics lab</strong> buzzed with potential, and <em>Chill Bill</em> ensured the perfect atmosphere to get things done.",
        "Stepping into <strong>Crash Space</strong> is like stepping into a realm of possibility. The <strong>laser cutter</strong> stood ready, the <strong>woodshop</strong> smelled like freshly sawed wood, and everything was in place to create something extraordinary."
        "You weren’t supposed to know, but there it was: a sudden hush in the workshop, tools left waiting, the door ajar like the universe just gave you a sign. No calendar, no plans—just you, the workbench, and a few hours of untold possibilities.",
        "I was just passing by when I noticed something... the workshop was unusually quiet, but not locked. A quick glance around and—yep—it’s open. No one’s watching, the tools are all yours. A brief window of opportunity before someone notices. What do you do with it?",
        "The schedule was blank, and no one mentioned it, but there it was—an open invitation to create, right in front of you. A few tools out of place, the hum of machines in the background, and that secret window where everything else stops. It’s yours, if you want it.",
        "I found myself drifting into the makerspace, half expecting the usual hustle, but instead—silence. The doors were open, but the schedule was empty. A rare slip in the timeline. A moment where everything felt... available. For once, there were no rules. No one was around to ask questions. Just tools and time.",
        "Walking past the club, I noticed the door—barely cracked open. A quiet call to action. The calendar didn’t say anything, but the space was wide open for the taking. I slipped inside, like I knew I wasn’t supposed to be here—but that’s exactly what made it exciting.",
        "I heard the hum before I saw the open door—something whispered to me to check. And there it was, an unannounced window in the schedule. No one had planned this. The tools were waiting, the clock was on pause, and I had the place to myself... just for a while.",
        "No meetings, no plans, no agenda... just a perfect moment where everything was empty, yet full of possibilities. I crept in quietly, not wanting to disturb the unexpected serenity of the space. The machines were calling—just a soft hum waiting for someone like me to take action.",
        "It wasn’t on any calendar, but somehow I knew—today was the day the makerspace was mine. A crack in the schedule, a rare slip of time where nothing was happening and everything was waiting. The perfect moment to make something that wasn’t supposed to happen.",
        "As I walked into the space, I noticed it right away—no one else, just me and the tools, like it was a private invitation. The schedule was clear, and that’s when I realized: I had stumbled into the open time no one planned for. Now I had to decide—what would I create with this secret window?",
        "There’s always that one moment where you don’t think it’s possible—yet here I am, in the makerspace with the door open wide, the clock not ticking, and no one around to ask questions. The perfect time to create something out of nothing. The only problem? No one else knows about this secret window.",
        "I wandered in, thinking I was late, but the space was eerily calm. The workstations were free, no one else around. For a second, I thought I’d stumbled into some alternate timeline where plans didn’t exist. I took a deep breath and knew this moment was mine.",
        "There’s a moment when the usual chaos of the space fades away. The calendar’s clear, and the machines seem to hum just for you. No one else is in the know, but you’re here, and it’s all yours. Just don’t let anyone catch wind of it.",
        "You could feel it before you even stepped inside—like a little pulse in the air. The makerspace was supposed to be empty, but the door was ajar. It wasn’t on anyone’s radar, but for a brief moment, it was all mine. Tools, time, and space to make whatever I wanted.",
        "I didn’t plan this, but somehow I found myself in the space at the right moment. The workshop was open without a whisper. No one knew, and the place was free, welcoming me like I was part of some secret project. What could I make in a space that was silently waiting for something to happen?",
        "The door was open—just enough for me to see the workstations unoccupied. A rare moment when the space was free, and time didn’t exist. I had no plans, but for some reason, that felt perfect. No one knew I was here, and that made it feel all the more exciting.",
        "I stepped into the space expecting the usual buzz, but all I found was an opportunity. No one had planned for this time, and the place was open, welcoming me like I was part of some hidden passageway into a world of creation. What would I make with this?",
        "The makerspace was quiet, almost too quiet. The schedule had a gap, and I had a feeling—just a hunch—that it was the perfect time to slip in unnoticed. The machines were still, waiting to be touched. What could I build in a place where time seemed to stand still?",
        "I wasn’t supposed to be here. There were no meetings, no plans on the board—but there it was, like an unlocked door to a secret garden. I slipped in, and the hum of machinery was the only sound. The schedule didn’t exist for this brief moment. What would I make?",
        "I found myself standing in the doorway, wondering if I’d misread something. No one else was around, and yet... the space was open, like I had unlocked some hidden time that no one knew about. The tools were calling me. What could I create here, now, when no one else is around?",
        "The machines were idle, the calendar clear. I slipped into the space without a sound. No one planned this time, but somehow it was mine for the taking. It was like stepping into a forgotten corner of the schedule, where only the makers could roam free.",
        "I crept into the workshop, half-expecting someone to stop me. But the place was wide open. A rare slip, a forgotten gap, and here I was. The tools didn’t mind, the clock didn’t care, and suddenly, I was alone in the space to make whatever I pleased.",
        "I wasn’t sure how it happened, but there I was—inside the makerspace with no one else around, the calendar totally free. It was like I had unlocked a secret opportunity—just me, the tools, and a fleeting moment to create something unexpected.",
        "You didn’t hear it from me, but there’s a little window of opportunity right now. The machines are idle, and the space is all yours if you’re quick. No meetings, no plans—just the freedom to build and create while no one’s looking.",
        "As the door swung open to <strong>Crash Space</strong>, it felt like stepping into a forgotten dimension where creativity flowed freely. <em>Chill Bill</em> hummed in the background, and the <strong>Prusa 3D printers</strong> whispered possibilities. No one had planned this moment, but I knew—this was a hidden opportunity.",
        "On <strong>Venice Blvd</strong>, the workshop felt like a secret haven, and the door to <strong>Crash Space</strong> opened just enough to offer a glimpse into a world of untold creation. The <strong>large meeting table</strong> lay waiting, ready to hold the plans for whatever adventure I could imagine.",
        "The air in <strong>Crash Space</strong> was charged, not just with electricity, but with the potential to build something extraordinary. <em>Chill Bill</em> softly purred, while the <strong>Prusa 3D printers</strong> stood at the ready, like guardians of invention. A rare slip in the schedule meant I had all the time to dream and create.",
        "I passed by <strong>Crash Space</strong> on <strong>Venice Blvd</strong>, and the door beckoned me in, not with a sound, but with a sense of endless possibility. The <strong>meeting table</strong> was unclaimed, the <strong>Prusa 3D printers</strong> idle, and the space was waiting—magically open just for me.",
        "In the quiet of <strong>Crash Space</strong>, I discovered the magic of untold possibilities. The hum of <em>Chill Bill</em> filled the air, while the <strong>Prusa 3D printers</strong> sat ready for anything. A rare window where no one had claimed the time, but the space was eager for someone to step in and create.",
        "I knew I shouldn’t have opened the door to <strong>Crash Space</strong>, but something drew me in. The <strong>large meeting table</strong> was still, the <strong>Prusa 3D printers</strong> seemed to hold their breath, and <em>Chill Bill</em> hummed in approval. Time was my ally, and I stepped in with a sense of adventure.",
        "As I entered <strong>Crash Space</strong>, I felt a shift in the air, like a spell had been cast. The <strong>Prusa 3D printers</strong> were waiting, like magical devices ready to bring ideas to life. <em>Chill Bill</em> kept the space cool, and the <strong>large table</strong> was ready for collaboration. No one else was around—it was my secret to make something new.",
        "I walked down <strong>Venice Blvd</strong> with no intention to enter <strong>Crash Space</strong>, but as the door opened, I felt the call of the unknown. The <strong>large meeting table</strong> stood waiting, the <strong>Prusa 3D printers</strong> glimmered like enchanted objects, and <em>Chill Bill</em> made sure the air was just right for creating something incredible.",
        "As I entered <strong>Crash Space</strong>, I couldn’t help but smile. The <strong>Prusa 3D printers</strong> were quietly waiting, the <strong>large meeting table</strong> was unclaimed, and <em>Chill Bill</em> whispered a welcoming hum. I had stumbled upon a secret time—an open moment where I could build anything my mind dreamed up.",
        "The <strong>large meeting table</strong> in <strong>Crash Space</strong> was the center of a quiet, magical world. The <strong>Prusa 3D printers</strong> were dormant, but the space was alive with potential, and <em>Chill Bill</em> kept it all cool, like a secret waiting to unfold. This wasn’t on the calendar, but it was the perfect moment to create.",
        "I had no plan to visit <strong>Crash Space</strong>, but the door creaked open, and I found myself drawn in. <em>Chill Bill</em> was... waiting.",
        "The schedule was blank, but the workbench was ready. It wasn’t planned, but that made it feel even more special. A quiet time when the workshop was ready for something unexpected. I had a feeling it was my turn to take over."])


    print(f'<h1>No Event: {title}</h1>\n<p>{descr}</p><hr>')
