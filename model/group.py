from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.id, self.name, self.header, self.footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
                    self.name == other.name or self.name[0:-1] == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, id=None, address=None, homephone=None,
                 mobilephone=None, workphone=None, secondaryphone=None, fax=None, all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.id = id
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (
                    self.lastname == other.lastname or self.lastname[0:-1] == other.lastname) \
               and (self.firstname == other.firstname or self.firstname[0:-1] == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


