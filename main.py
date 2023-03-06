from home_work2 import seminar6, seminar7, home_work1

path = 'c:/temp'

seminar6.make_files('bin', count=10)
seminar6.maker(zip=2, jpg=3, png=4, avi=3, doc=2, txt=3, mp4=3)
seminar6.maker(zip=2, jpg=3, png=4, avi=3, doc=2, txt=3, mp4=3, path=path)

seminar7.sort_files(path)

home_work1.renamer(path, result_name='new', counter_length=10, result_ext='log', start=3, stop=6)