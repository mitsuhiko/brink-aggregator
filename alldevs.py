DEVS = [
    ('Paul Wedgwood', 'Locki', 'CEO and Game Director'),
    ('Arnout van Meer', 'RR2DO2', 'Technical Director'),
    ('Richard Jolly', 'Fluffy_gIMp', 'Media Director'),
    ('Angelo Dal Pra', 'classact', 'Environment Artist'),
    ('Arne Olav Hallingstad', 'ao', 'Programmer'),
    ('Aubrey Hesselgren', 'Bezzy', 'Technical Game Designer'),
    ('Ben Davis', 'mantegra', 'Character Artist'),
    ('Ben Hopkinson', 'Randles', 'IT Manager'),
    ('Boris Lowinger', 'Zobbo', 'Animator'),
    ('Chris Bull', 'Hauser', 'Animator'),
    ('Chris Sweetman', 'peaceful warrior', 'Audio Director'),
    ('Craig Nelson', 'Madcat', 'Senior IT Analyst'),
    ('Dann Yeung', 'SRS-Kap', 'Lead Gameplay Programmer'),
    ('Dave Johnston', 'Captain ducks', 'Senior Level Designer'),
    ('David Edwards', 'Davros', 'Level Designer'),
    ('Dean Calver', 'Deano', 'Lead Programmer'),
    ('Digby Murray', 'SirDigga', 'Production Tester'),
    ('Ed B Reid', 'mred', 'Online Services Programmer'),
    ('Edward Stern', 'Bongoboy', 'Lead Writer'),
    ('Fabrice Bouvet', 'faaab', 'Lead Animator'),
    ('Georgi Simeonov', 'Calader', 'Concept Artist'),
    ('Gordon Biggans', 'digibob', 'Senior Programmer'),
    ('Jamie Manson', 'Fishbus', 'Level Designer'),
    ('Jared Hefty', 'jRAD', 'Lead Tools Programmer'),
    ('Jaromir Salaj', 'pg', 'Artist'),
    ('Jeremy Hay', 'pinflux', 'Media Artist'),
    ('Jiri Kristek', 'JFK', 'Associate Producer'),
    ('Joe Gibson', 'Rex-TheGrunt', 'IT Support Engineer'),
    ('John Molloy', 'nifty', 'Game Designer'),
    ('Jonas Nelson', 'suctionlord', 'Programmer'),
    ('Laurel Austin', 'Tully', 'Senior Concept Artist'),
    ('Lloyd Morris', 'LloydM', 'Level Designer'),
    ('Matt Lowe', 'Anti', 'Associate Producer'),
    ('Matt McDaid', 'Taff', 'Senior Environment Artist'),
    ('Mikkel Gjoel', 'mig', 'Programmer'),
    ('Miroslav Slowik', 'Draska', 'Level Designer'),
    ('Neil Alphonso', 'exedore', 'Lead Game Designer'),
    ('Oliver Jauncey', 'Kensai', 'Senior Programmer'),
    ('Olivier Leonardi', 'nosebone', 'Art Director'),
    ('Paul Greveson', 'MoP', 'Technical Artist'),
    ('Paul Saunders', 'digs', 'Senior Designer'),
    ('Pete Loveridge', 'Dusk777', 'Production Tester'),
    ('Phil Barnell', 'pipster', 'Production Tester'),
    ('Pierre Tregaro', 'trega', 'Programmer'),
    ('Radek Szczepanczyk', 'ElDonaldo', 'Artist'),
    ('Rav Channa', 'ioli', 'HR Manager'),
    ('Richard Ham', 'Rahdo', 'Creative Director'),
    ('Robert Macdonald', 'Mac', 'UI Programmer'),
    ('Robert Watkins', 'woko', 'Lead Environment Artist'),
    ('Ronald Koppers', 'Conine', 'PlayStation Programmer'),
    ('Sean Francis', 'Poons', 'Production Tester'),
    ('Simon Price', 'Bazee', 'Audio Programmer'),
    ('Simon Batty', 'Lianshi', 'Production Tester'),
    ('Stephen Etheridge', 'Crispy', 'Lead Tester'),
    ('Stephen Gaffney', 'malarky', 'Studio Director'),
    ('Steve Alves', 'Citrusy', 'Production Tester'),
    ('Steve Hessel', 'badman', 'Community Relations Manager'),
    ('Terry Seidler', 'Salteh', 'Occasional Honourary Intern Associate Producer'),
    ('Tibor Toth', 'iib', 'Senior Environment Artist'),
    ('Tim Appleby', 'spacemonkey', 'Lead Character Artist'),
    ('Tim Rose', 'Huntle', 'Associate Producer'),
    ('William Richens', 'Smooth', 'Associate Producer')
]


def install():
    import brink
    for name, nick, description in DEVS:
        dev = brink.Developer(name, forum_name=nick)
        dev.description = '<p>' + description
        brink.db.session.add(dev)
    brink.db.session.commit()


if __name__ == '__main__':
    install()
