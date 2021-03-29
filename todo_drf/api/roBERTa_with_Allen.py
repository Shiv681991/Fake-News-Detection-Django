from allennlp.predictors.predictor import Predictor
import allennlp_models.nli
# predictor = Predictor.from_path("/snli-roberta-large-2020.02.27.tar.gz", predictor_name="textual-entailment")
predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/snli-roberta-large-2020.02.27.tar.gz", predictor_name="textual-entailment")

answer=predictor.predict(
  hypothesis="Two women are sitting on a blanket near some rocks talking about politics.",
  premise="Two women are wandering along the shore drinking iced tea."
)
print(answer)