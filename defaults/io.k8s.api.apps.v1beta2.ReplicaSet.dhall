{ apiVersion =
    "apps/v1beta2"
, kind =
    "ReplicaSet"
, metadata =
    ./io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta.dhall
, spec =
    None ./../types/io.k8s.api.apps.v1beta2.ReplicaSetSpec.dhall
, status =
    None ./../types/io.k8s.api.apps.v1beta2.ReplicaSetStatus.dhall
}
