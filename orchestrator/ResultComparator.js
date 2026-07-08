
class ResultComparator {
    compare(results) {
        results.sort(
            (a, b) => b.accuracy - a.accuracy
        );

        return {
            rankings: results,
            bestModel: results[0]
        };
    }

}

export default ResultComparator; 