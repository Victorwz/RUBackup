import DAO
import Scanner
# Checking md5 doesn't reflect file name change
if __name__ == '__main__':
    path = "/Users/hanmufu/Downloads"
    user = 'cqh'
    pwd = 'CAMRYLOVESEDGE'
    ftp_user = 'root'
    ftp_pwd = 'CAMRYLOVESEDGE'
    port = 22

    db = 'tommy'
    s = Scanner.Scanner(path, db, user, pwd, ftp_user, ftp_pwd, port)

