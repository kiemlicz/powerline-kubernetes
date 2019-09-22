# vim:fileencoding=utf-8:noet:tabstop=4:softtabstop=4:shiftwidth=4:expandtab:
import os
from powerline.theme import requires_segment_info
from powerline.segments import Segment, with_docstring
from kubernetes.config import list_kube_config_contexts
from kubernetes.config.kube_config import ENV_KUBECONFIG_PATH_SEPARATOR

_KUBERNETES = u'\U00002388 '


@requires_segment_info
class KubernetesSegment(Segment):

    def kube_logo(self, color):
        return {
            'contents': _KUBERNETES,
            'highlight_groups': [color],
            'divider_highlight_group': 'kubernetes:divider'
        }

    def build_segments(self, context, namespace):
        alert = (namespace in self.alerts or context + ':' + namespace in self.alerts)
        segments = []

        if self.show_cluster:
            color = 'kubernetes_cluster:alert' if alert else 'kubernetes_cluster'
            if self.show_kube_logo:
                segments.append(self.kube_logo(color))

            segments.append({
                'contents': context,
                'highlight_groups': [color],
                'divider_highlight_group': 'kubernetes:divider'
            })

        if self.show_namespace:
            color = 'kubernetes_namespace:alert' if alert else 'kubernetes_namespace'

            if namespace != 'default' or self.show_default_namespace:
                if not self.show_cluster and self.show_kube_logo:
                    segments.append(self.kube_logo(color))

                segments.append({
                    'contents': namespace,
                    'highlight_groups': [color],
                    'divider_highlight_group': 'kubernetes:divider'
                })

        return segments

    def __init__(self):
        self.pl = None
        self.show_kube_logo = None
        self.show_cluster = None
        self.show_namespace = None
        self.show_default_namespace = None
        self.alerts = []

    def __call__(
            self,
            pl,
            show_kube_logo=True,
            show_cluster=True,
            show_namespace=True,
            show_default_namespace=False,
            alerts=[],
            **kwargs
        ):
        pl.debug('Running powerline-kubernetes')
        segment_info_envs = kwargs['segment_info']['environ']
        # non existing location in case KUBECONFIG is not present, not defaulting to ~/.kube/config
        kubeconfig_location = segment_info_envs['KUBECONFIG'] if 'KUBECONFIG' in segment_info_envs else ''

        self.pl = pl
        self.show_kube_logo = show_kube_logo
        self.show_cluster = show_cluster
        self.show_namespace = show_namespace
        self.show_default_namespace = show_default_namespace
        self.alerts = alerts

        config_locations_list = kubeconfig_location.split(ENV_KUBECONFIG_PATH_SEPARATOR)
        if next(os.path.exists(e) for e in config_locations_list):
            try:
                loc = next(iter(config_locations_list))
                contexts, current_context = list_kube_config_contexts(config_file=loc)
                ctx = current_context['context']
                context = current_context['name']
                namespace = ctx['namespace'] if 'namespace' in ctx else 'default'
            except Exception as e:
                pl.error(e)
                return
            return self.build_segments(context, namespace)
        else:
            return []


kubernetes = with_docstring(KubernetesSegment(),
'''Return the current context.

It will show the current context in config.
It requires kubectl and kubernetes to be installed.

Divider highlight group used: ``kubernetes:divider``.

powerline-daemon must be run since import from kubernetes is terribly slow

Highlight groups used: ``kubernetes_cluster``,
``kubernetes_cluster:alert``, ``kubernetes_namespace``,
and ``kubernetes_namespace:alert``, .
''')
