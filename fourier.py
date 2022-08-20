from manim import *
class FourierScene(Scene):
    CONFIG={
        'n_vectors':10
    }
    def construct(self):
        self.add_vectors_circles_path()
        self.play(Write(Tex('Ricardo')))
    def add_vectors_circles_path(self):
        text_mob=Tex(r'\rm M', fill_opacity=0, stroke_width=1,stroke_color=WHITE)
        text_mob.set_height(6)
        path=text_mob.family_members_with_points()[0]
        freqs=None
        if freqs is None:   #get_coeff_of_path
            n=self.CONFIG['n_vectors']
            all_freqs=list(range(n//2,-n//2,-1))
            all_freqs.sort(key=abs)
            return all_freqs
        dt=1/10000
        ts=np.arrange(0,1,dt)
        samples=np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples-=ORIGIN
        complex_samples=samples[:,0]
        