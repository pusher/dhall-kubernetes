{ conditions :
    List ./io.k8s.api.apps.v1beta2.ReplicaSetCondition.dhall
, replicas :
    Natural
, availableReplicas :
    Optional Natural
, fullyLabeledReplicas :
    Optional Natural
, observedGeneration :
    Optional Natural
, readyReplicas :
    Optional Natural
}
