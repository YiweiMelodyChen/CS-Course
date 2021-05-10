class User:
    """A User can attend a Meeting.

    >>> john = User('denero@berkeley')
    >>> oski = User('oski@berkeley')
    >>> jack = User('jack@junioruniversity')
    >>> section = Meeting(john)
    >>> for x in [john, oski, jack]:
    ...     x.attend(section)
    >>> section.accepted
    [User('denero@berkeley')]
    >>> section.requested
    [User('oski@berkeley'), User('jack@junioruniversity')]

    >>> oski.attend(section)
    oski@berkeley is already attending

    >>> section.admit(lambda x: 'berkeley' in x.identifier)
    >>> section.accepted
    [User('denero@berkeley'), User('oski@berkeley')]
    >>> section.requested
    [User('jack@junioruniversity')]

    >>> oski.attend(section)
    oski@berkeley is already attending
    >>> User('denero@berkeley').attend(section) # A different user with the same identifier can attend
    >>> section.requested
    [User('jack@junioruniversity'), User('denero@berkeley')]
    """
    """Implement the methods of the User and Meeting classes as follows:

When a User decides to attend a Meeting for the first time, if they are the host of the Meeting, they will be added to the end of the accepted list; otherwise they will be added to the end of the requested list.

When a User attempts to attend a meeting again, they are not added to any list. A string is returned stating that the User is already attending.

A Meeting’s admit method takes a function f that takes a User and returns whether they should be admitted. The admit method moves all requested Users for which f returns a true value from the requested list to the end of the accepted list."""
    def __init__(self, identifier):

        self.identifier = identifier

    def attend(self, meeting):

        if self.identifier in meeting.requested + meeting.accepted:

            print(self.identifier, 'is already attending')

        else:

            users = meeting.requested

            if self.identifier == meeting.host:

                users = meeting.accepted

            users.append(self.identifier)

    def __repr__(self):

        return 'User(' + repr(self.identifier) + ')'

class Meeting:
    """A Meeting can admit requested Users."""
    def __init__(self, host):
        self.requested = []
        self.accepted = []
        self.host = host

    def admit(self, f):

        for x in self.requested:

            if f(x):

                self.accepted.append(x)

        self.requested = [requested for requested in self.requested if f(requested) is False]